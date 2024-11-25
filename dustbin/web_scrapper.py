from llama_index.core.tools import FunctionTool
from bs4 import BeautifulSoup
import requests

def web_scrapper_fun(url):
    try:
        response = requests.get(url)
        return response#{"web_content": response}
    except Exception as e:
        return {"error": str(e)}
    


web_scrapper = FunctionTool.from_defaults(
    fn = web_scrapper_fun,
    name = "web_scrapper",
    description= "This tool can scrap the data from internet and scrap the pages from the internet for further use of the data present"
)

res = web_scrapper_fun("https://paytm.com/movies/aurangabad")
print(res)