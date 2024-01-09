import pathlib
import json
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


with open("configs.json", "r", encoding="utf8") as fp:
    configs = json.load(fp)


GEMINI_SAFETY_SETTINGS = configs["GEMINI_SAFETY_SETTINGS"]
GEMINI_GENERATION_CONFIG = configs["GEMINI_GENERATION_CONFIG"]
GEMINI_MEMORIES_CAPACITY = configs["GEMINI_MEMORIES_CAPACITY"]


BASE_DIR = pathlib.Path(__file__).parent
COGS_DIR = BASE_DIR / "cogs"
LOGS_DIR = BASE_DIR / "logs"