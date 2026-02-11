from langchain_core.language_models.llms import LLM
from typing import Optional, List, Any, Dict
import requests

# =========================
# Customable LLM using API
# =========================
class MyCustomLLM(LLM):
    api_url: str
    api_key: str
    model: str = "google/gemma-3-4b-it:free"

    @property
    def _llm_type(self) -> str:
        return "openrouter-custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Ambil teks hasil dari format OpenRouter
        return data["choices"][0]["message"]["content"]