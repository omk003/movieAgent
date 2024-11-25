import json
from llama_index.core.tools import FunctionTool


def get_seat_details(city, movie_name, cinema_name, showtime):
    with open('./data/movies_data.json', 'r') as f:
        data = json.load(f)

    res = data['bengaluru']['Bhairathi Ranagal']['cinemas'][0]['showtimes'][0]
    print(res)
    try:
        # Access the city data
        city_data = data.get(city)
        if not city_data:
            return f"City '{city}' not found."
        
        # Access the movie data
        movie_data = city_data.get(movie_name)
        if not movie_data:
            return f"Movie '{movie_name}' not found in city '{city}'."
        
        # Find the cinema
        cinemas = movie_data.get("cinemas", [])
        cinema = next((c for c in cinemas if c["cinema_name"] == cinema_name), None)
        if not cinema:
            return f"Cinema '{cinema_name}' not found for movie '{movie_name}'."
        
        # Filter showtimes by the specified showtime
        showtimes = cinema.get("showtimes", [])
        print(showtimes)
        filtered_showtimes = [
            {
                "showtime": st["showtime"],
                "screen": st["screen"],
                "seats": st["seats"]
            }
            for st in showtimes
            if st["showtime"] == showtime
        ]
        
        if not filtered_showtimes:
            return f"Showtime '{showtime}' not found in cinema '{cinema_name}'."
        
        return filtered_showtimes
    
    except Exception as e:
        return {"error": str(e)}

st = get_seat_details("bengaluru","Bhairathi Ranagal", "Cinepolis ETA Namma Mall, Binny Pete, Bengaluru","19:30")
print(st)

seat_reader = FunctionTool.from_defaults(
    fn = get_seat_details,
    name = "seat_reader",
    description= "use this tool when you want showtimes of movies by cinema , it will take input like {movie_name,cinema} "
)