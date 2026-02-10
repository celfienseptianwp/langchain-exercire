from dotenv import load_dotenv
from typing import Optional, List, Any, Dict
import requests
from langchain_core.language_models.llms import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

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

# =========================
# Task for LLM
# =========================
def generate_pet_name(animal_type, pet_color):
    parser = StrOutputParser()

    # LLM Wrappers
    llm = MyCustomLLM(
        api_url=os.getenv("API_URL"),
        api_key=os.getenv("API_KEY"),
        model=os.getenv("MODEL")
    )

    # Prompt Templates
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} and I want a cool name for it, it is {pet_color} in color. Suggest three cool names without any explanation"
    )
    
    # Chains
    name_chain = prompt_template_name | llm | parser
    response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

    return response

if __name__ == "__main__":
    print(generate_pet_name("dragon", "red"))