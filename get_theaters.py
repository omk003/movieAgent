import json
from llama_index.core.tools import FunctionTool

def get_theaters_with_showtimes(movie_name, city="bengaluru"):
    with open('./data/movies_data.json', 'r') as f:
        data = json.load(f)

    theaters_with_showtimes = []
    for cinema in data[city][movie_name]['cinemas']:
        for showtime in cinema['showtimes']:
            theaters_with_showtimes.append(f"{cinema['cinema_name']} - {showtime['showtime']}")

    return {"cinema_with showtimes":theaters_with_showtimes}


cinema_showtime_reader = FunctionTool.from_defaults(
    fn = get_theaters_with_showtimes,
    name = "cinema_reader",
    description= "use this tool when you want cinema for particular movies or cinema with there showtimes, and also give argument of movie name "
)