import json
from llama_index.core.tools import FunctionTool

def get_movie_names():
    city = "bengaluru"
    with open('./data/movies_data.json', 'r') as f:
        data = json.load(f)

    return {"movies_list": list(data[city].keys())}



movie_reader = FunctionTool.from_defaults(
    fn = get_movie_names,
    name = "movie_reader",
    description= "use this tool when you want list movies only, it doesnt take any inputs , it only gives list of movies "
)
