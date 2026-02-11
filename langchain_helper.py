from dotenv import load_dotenv
from llm_wrapper import MyCustomLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()

# ===========================
# Task for LLM via LangChain
# ===========================
def generate_pet_name(animal_type, pet_color):
    parser = StrOutputParser()

    # LLM Wrappers
    llm = MyCustomLLM(
        api_url = os.getenv("API_URL"),
        api_key = os.getenv("API_KEY"),
        model = os.getenv("MODEL")
    )

    # Prompt Templates
    prompt_template_name = PromptTemplate(
        input_variables = ["animal_type", "pet_color"],
        template = "I have a {animal_type} and I want a cool name for it, it is {pet_color} in color. Suggest three cool names without any explanation"
    )
    
    # Chains
    name_chain = prompt_template_name | llm | parser
    response = name_chain.invoke({"animal_type": animal_type, "pet_color": pet_color})

    return response

# =========================
# LLM Agents via LangChain
# =========================
@tool
def multiply(a: float, b: float) -> float:
    "Multiply two numbers"
    return a * b

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper
)

tools = [wikipedia, multiply]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Use tools when necessary to answer questions."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

def langchain_agent():
    # LLM Wrappers
    llm = MyCustomLLM(
        api_url = os.getenv("API_URL"),
        api_key = os.getenv("API_KEY"),
        model = os.getenv("MODEL")
    )
    
    # Agents
    agent = create_react_agent(
        model = llm,
        tools = tools,
        prompt = prompt
    )

    # Executor
    executor = AgentExecutor(
        agent = agent,
        tools = tools,
        verbose = True
    )

    # Run
    result = executor.invoke({
        "input": "What is the average age of a dog? Multiply age by 3"
    })

    print(result["output"])

if __name__ == "__main__":
    # print(generate_pet_name("dragon", "red"))
    langchain_agent()