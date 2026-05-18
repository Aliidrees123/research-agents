from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv(override=True)

@dataclass
class Config:
    model: str

    @classmethod
    def from_env(cls):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key missing from .env")
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

        return Config(model=model)
