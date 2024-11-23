from llama_index.core.tools import FunctionTool
from duckduckgo_search import DDGS




def web_search_fun(query):
    try:
        results = DDGS().text(query, max_results=5)
        return {"web_content": results}
    except Exception as e:
        return {"error": str(e)}
    


web_reader = FunctionTool.from_defaults(
    fn = web_search_fun,
    name = "web_reader",
    description= "This tool can read and extract data from internet and websites and return the results. Use this when you need to search on internet"
)