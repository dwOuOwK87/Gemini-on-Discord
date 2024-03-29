import discord
from discord.ext import commands
import google.generativeai as genai
from typing import Optional
import requests
from PIL import Image
from io import BytesIO

import settings

from src.gemini import Gemini
from src.model import GeminiModel
from src.memory import Memory
from src.logger import logger


class GenerativeAI(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.gemini = Gemini(
            model=GeminiModel(
                api_key=settings.GEMINI_API_KEY,
                text_engine=genai.GenerativeModel(
                    model_name="gemini-pro",
                    safety_settings=settings.GEMINI_SAFETY_SETTINGS,
                    generation_config=settings.GEMINI_GENERATION_CONFIG
                ),
                vision_engine=genai.GenerativeModel(
                    model_name="gemini-pro-vision",
                    safety_settings=settings.GEMINI_SAFETY_SETTINGS,
                    generation_config=settings.GEMINI_GENERATION_CONFIG
                )
            ),
            memory=Memory(settings.GEMINI_MEMORIES_CAPACITY)
        )


    @discord.app_commands.command(name="reset", description="Reset memories")
    async def reset(self, interaction: discord.Interaction):
        if interaction.user == self.bot.user:
            return
        
        self.gemini.clear_memory(interaction.user.id)
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f'**Reset Gemini conversation history**')

        logger.info(f"User '{interaction.user.name}' used 'reset'")


    @discord.app_commands.command(name="chat", description = "Chat with generative AI")
    @discord.app_commands.describe(message = "message...")
    async def chat(self, interaction: discord.Interaction, message: str):
        if interaction.user == self.bot.user:
            return
        
        await interaction.response.defer()

        message = message.strip()
        response = await self.gemini.get_response(interaction.user.id, message)

        await interaction.followup.send(f'### - You Asked:\n{message}\n### - Response:\n{response}')

        logger.info(f"User '{interaction.user.name}' used 'chat'")
        

    
    @discord.app_commands.command(name="see", description = "Make generative AI read image")
    @discord.app_commands.describe(image = "attachment...", message = "message...")
    async def see(self, interaction: discord.Interaction, image: discord.Attachment, message: Optional[str]):
        if interaction.user == self.bot.user:
            return
        
        await interaction.response.defer()

        if message is not None:
            message = message.strip()

        image_object = Image.open(BytesIO(requests.get(image.url).content))
        response = await self.gemini.get_response_from_image(message, image_object)

        if message is not None:
            await interaction.followup.send(f'### - You Asked:\n{message}\n### - Response:\n{response}\n\n{image.url}')
        else:
            await interaction.followup.send(f"### - Response:\n{response}\n\n{image.url}")

        logger.info(f"User '{interaction.user.name}' used 'see'")
        

           
async def setup(bot: commands.Bot):
    await bot.add_cog(GenerativeAI(bot))