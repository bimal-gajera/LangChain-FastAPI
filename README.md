# LangChain FastAPI with GPT and LLaMA

This project implements a FastAPI server that utilizes OpenAI's GPT and LLaMA3.2 models to provide code generation and computer science explanations through a web interface.

Ollama is a framework designed for running large language models locally, and in this project, it is used for LLaMA3.2 inference.

Models Used
- **OpenAI GPT**: Used for generating Python code.
- **Ollama LLaMA-3.2:1b**: Used for providing explanations in the context of computer science.


### env setup
To run the code, create a file `.env` in the project folder and write all the API keys in this file.

For reference,
```
LANGCHAIN_API_KEY = "key1"
OPENAI_API_KEY = "key2"
LANGCHAIN_PROJECT = "Name of the project"
```


Run the FastAPI server:
```
python app.py
```

Run the Streamlit client:
```
streamlit run client.py
```