import discord
from discord.ext import commands

import settings
from src.server import keep_alive


bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
            
    
@bot.event
async def on_ready():

    await bot.wait_until_ready()

    for cogs_file in settings.COGS_DIR.glob("*.py"):
        if cogs_file.name != "__init__.py":
            await bot.load_extension(f"cogs.{cogs_file.name.removesuffix('.py')}")

    await bot.tree.sync()

    print(f'We have logged in as {bot.user}')


@bot.tree.error
async def on_tree_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    print(error)
    await interaction.followup.send('> **Error: Something went wrong, please try again later!**')
    

if __name__ == "__main__":
    #　keep_alive()
    bot.run(settings.DISCORD_API_KEY)