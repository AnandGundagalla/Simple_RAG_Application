# llm_provider.py

import google.generativeai as genai
from langchain_core.language_models.llms import LLM
from typing import Optional, List
from pydantic import Field
import config


class GeminiLLM(LLM):
    # Declare Pydantic fields
    model_name: str = Field(default=config.LLM_MODEL)
    api_key: str = Field(default=config.GEMINI_API_KEY)
    model: Optional[genai.GenerativeModel] = None  # declare field

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configure Gemini API
        genai.configure(api_key=self.api_key)

        # Pydantic-safe: assign using object.__setattr__
        object.__setattr__(self, "model", genai.GenerativeModel(self.model_name))

    @property
    def _llm_type(self) -> str:
        return "gemini_llm"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.model.generate_content(prompt)
        return response.text


def get_llm():
    return GeminiLLM()
