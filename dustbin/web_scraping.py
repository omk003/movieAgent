from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent


from dustbin.web_scrapper import web_scrapper
from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

llm = Ollama(model="llama3.2", request_timeout=30.0)

tools = [
    web_scrapper,
]

context = """"Your task is assist the user and answer there questions, you are a helpful assistant. your main goal is to give user information about movies or which movies are available now and genre of that movie"""

agent  = ReActAgent.from_tools(tools,llm=llm, verbose=True, context=context, max_iterations=10)

result = agent.query("which movies are in the market now and i want direct links to the movie booking page, hint paytm")

print(result)

