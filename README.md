# $\text{LangChain}$

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-0FA958?logo=chainlink&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)

**LangChain** is an open-source framework that enables developers working with AI to integrate LLMs such as Chat-GPT with external computation and data sources. 

**LangChain** Documentation: `python.langchain.com`

Three important concepts in LangChain:
1. Components: Allow us to connect with LLMs such as Chat-GPT or HuggingFace (LLM Wrappers), enable us to avoid manually writing text for LLM input (Prompt Templates), and allow us to extract relevant information for LLMs (Indexes for information retrieval).
2. Chains: (Assemble components to solve a specific task)
3. Agents: (Agents allow LLMs to interact with their environment)

## $\text{Procedure for Creating a Project Directory}$
In PowerShell:
1. `cd D:\Schrodie\My Projects\`
2. `mkdir langchain-exercise`
3. `cd .\langchain-exercise\`
4. `code .`

## $\text{Procedure for Creating a Virtual Environment}$
In VSCode Terminal:
1. `python -m venv .venv` to create virtual environment .venv
2. `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` to get access to PowerShell
3. `.venv\Scripts\Activate.ps1` to activate virtual environment
4. `pip install langchain openai streamlit python-dotenv` to install independences

## $\text{Procedure for Running Streamlit}$
In VSCode Terminal:
1. `streamlit run main.py` to open the GUI  
2. `ctrl + c` to stop the GUI

## $\text{References}$
[1] LangChain Crash Course for Beginners. YouTube. Available in: https://youtu.be/lG7Uxts9SXs
