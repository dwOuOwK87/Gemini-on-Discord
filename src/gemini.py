from src.memory import MemoryInterface
from src.model import ModelInterface
from PIL.Image import Image
from typing import Optional


class Gemini:

    def __init__(self, model: ModelInterface, memory: MemoryInterface):
        self.model = model
        self.memory = memory

    async def get_response(self, user_id: int, message: str):
        content = {"role": "user", "parts": [message]}
        response = await self.model.chat_completion(self.memory.get(user_id) + [content]) 

        # If chat_completion doesn't raise Exception, append contents to the memory
        self.memory.append(user_id, content, {"role": "model", "parts": [response]})

        return response
    
    async def get_response_from_image(self, message: Optional[str], image: Image):
        response = await self.model.read_image(message, image)
        return response


    def clear_memory(self, user_id: int):
        self.memory.remove(user_id)