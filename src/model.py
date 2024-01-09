from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import google.generativeai as genai
from PIL.Image import Image


class ModelInterface(ABC):

    @abstractmethod
    async def chat_completion(self, contents: List[Dict]) -> str:
        pass

    
    @abstractmethod
    async def read_image(self, message: Optional[str], image: Image) -> str:
        pass

    
    

class GeminiModel(ModelInterface):

    def __init__(self, api_key: str, text_engine: genai.GenerativeModel, vision_engine: genai.GenerativeModel):
        genai.configure(api_key=api_key)
        self.text_engine = text_engine
        self.vision_engine = vision_engine


    async def chat_completion(self, contents: List[Dict]) -> str:
        response = await self.text_engine.generate_content_async(contents)
        return response.text
    

    async def read_image(self, message: Optional[str], image: Image) -> str:
        if message is None:
            response = await self.vision_engine.generate_content_async(image)
            return response.text

        response = await self.vision_engine.generate_content_async([message, image])
        await response.resolve()
        return response.text