import json
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


# Data changes frequently
# currently using to minize the info , takes url and give data for that movie
def get_city_data(url):
    json_data = fetch_json_from_url(url)
    if json_data:
        movie_name = json_data['meta']['movies'][0]['name']
        movie_type = ", ".join(json_data['meta']['movies'][0]['grn'])

        output_data = {
            "movie_name": movie_name,
            "movie_type": movie_type,
            "cinemas": []
        }

        for i, cinema_id in enumerate(json_data['data']['cinemasOrder']):
            cinema_name = json_data['meta']['cinemas'][i]['name']
            show_time = json_data['meta']['filterData']['showTimeList'][i]

            cinema_info = {
                "cinema_name": cinema_name,
                "showtimes": []
            }

            showtime_info = {
                        "showtime": show_time,
                    }
            cinema_info['showtimes'].append(showtime_info)

            output_data['cinemas'].append(cinema_info)

        return output_data
    


def fetch_json_from_url(url):
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error fetching data from {url}: {response.text}")
    return None

# first function to run which takes list of urls and give output as dict so later conversion into json
def get_data_for_all_movie(url_list):
    documents = {}
    for url in url_list:
        documents[get_city_data(url)["movie_name"]] = get_city_data(url)
    return documents




# It fetches movie code for the given city , which are then required to extract data for specific movies by codes
def extract_movieCodes(city):
    city = city.lower()
    url = f"https://paytm.com/movies/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script_tag = soup.find('script', id='__NEXT_DATA__')
        script_text = script_tag.text
        json_data = json.loads(script_text)
        movie_codes = []

        try:
            # Traverse the JSON structure to access movieCode values
            movies = json_data["props"]["pageProps"]["initialState"]["movies"]["currentlyRunningMovies"][city]["data"]["groupedMovies"]
            for movie in movies:
                for lang_format_group in movie["languageFormatGroups"]:
                    for screen_format in lang_format_group["screenFormats"]:
                        movie_code = screen_format["movieCode"]
                        if movie_code != "Error":
                            movie_codes.append(movie_code)
        except:
            return {"Error, no cities found or url is invalid"}

        return movie_codes 


    else:
        print(f"Error fetching data from {url}:{response.status_code}")
        return None
    




# it returns the data of all movies available in the given city
def get_moviedata_by_city(city):
    documents = {}
    movieCodes = extract_movieCodes(city)
    for code in movieCodes:
        
        url = f'https://apiproxy.paytm.com/v3/movies/search/movie?meta=1&reqData=1&city={city}&movieCode={code}&version=3&site_id=1&channel=HTML5&child_site_id=1&client_id=paytm&clientId=paytm#'
        if get_city_data(url):
            documents[get_city_data(url)["movie_name"]] = get_city_data(url)
        

    return documents


#for all cities, 
def get_all_movie_data(city_list):
    documents = {}
    for city in city_list:
        documents[city] = get_moviedata_by_city(city)
        print(f"done for {city}")
        # time.sleep(7)
    today = datetime.today().strftime('%Y%m%d')
    with open(f'data/movies_data_constant.json', 'w') as outfile:
        json.dump(documents, outfile, indent=4)


# All this funtions above fetch data that might change not frequently like seats ^

# city_list = ["pune", "aurangabad", "bengaluru", "mumbai"]

# Data that changes frequently
#take url of movie and give output as dict
def format_movie_data_alpha(url):

    json_data = fetch_json_from_url(url)
    if json_data:
        movie_name = json_data['meta']['movies'][0]['name']
        movie_type = ", ".join(json_data['meta']['movies'][0]['grn'])

        output_data = {
            "movie_name": movie_name,
            "movie_type": movie_type,
            "cinemas": []
        }

        for i, cinema_id in enumerate(json_data['data']['cinemasOrder']):
            cinema_name = json_data['meta']['cinemas'][i]['name']
            show_time = json_data['meta']['filterData']['showTimeList'][i]

            cinema_info = {
                "cinema_name": cinema_name,
                "showtimes": []
            }

            for show in json_data['pageData']['sessions'][str(cinema_id)]:
                screen_name = show['audi']

                for area in show['areas']:
                    seat_type = area['label']
                    available_seats = area['sAvail']
                    total_seats = area['sTotal']
                    price = area['price']

                    showtime_info = {
                        "showtime": show_time,
                        "screen": screen_name,
                        "seats": {
                            "seat_type": seat_type,
                            "available_seats": available_seats,
                            "total_seats": total_seats,
                            "price": price
                        }
                    }
                    cinema_info['showtimes'].append(showtime_info)

            output_data['cinemas'].append(cinema_info)

        return output_data
    

def get_data_for_all_movie_alpha(url_list):
    documents = {}
    for url in url_list:
        documents[format_movie_data_alpha(url)["movie_name"]] = format_movie_data_alpha(url)
    return documents

def get_moviedata_by_city_alpha(city):
    documents = {}
    movieCodes = extract_movieCodes(city)
    for code in movieCodes:
        
        url = f'https://apiproxy.paytm.com/v3/movies/search/movie?meta=1&reqData=1&city={city}&movieCode={code}&version=3&site_id=1&channel=HTML5&child_site_id=1&client_id=paytm&clientId=paytm#'
        if get_city_data(url):
            documents[format_movie_data_alpha(url)["movie_name"]] = format_movie_data_alpha(url)
        

    return documents

#for all cities, 
def get_all_movie_data_alpha(city_list):
    documents = {}
    for city in city_list:
        documents[city] = get_moviedata_by_city_alpha(city)
        print(f"done for {city}")
        # time.sleep(7)
    today = datetime.today().strftime('%Y%m%d')
    with open(f'data/movies_data_complete.json', 'w') as outfile:
        json.dump(documents, outfile, indent=4)


# for constant data / update per day
list_a = ["bengaluru"]
get_all_movie_data(list_a)

# Data that changes like seats
city_list = ["bengaluru"] #["pune", "aurangabad", "bengaluru", "mumbai"]
get_all_movie_data_alpha(city_list)