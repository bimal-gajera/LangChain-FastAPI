from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="API Server"
)

gpt_llm = ChatOpenAI()
llama_llm = OllamaLLM(model="llama3.2:1b")

prompt1 = ChatPromptTemplate.from_template("Write a python code to solve {topic} problem.")
prompt2 = ChatPromptTemplate.from_template("Briefly explain {topic} in context of computer science.")

add_routes(app, prompt1|gpt_llm, path="/code-generator")
add_routes(app, prompt2|llama_llm, path="/cs-guide")




if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)