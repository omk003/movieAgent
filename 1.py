import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = "https://paytm.com/movies/aurangabad"

# Fetch the HTML content from the URL
response = requests.get(url)
required = response.text[22000:45000] 

file_path = "data/scraping_code.txt"
with open(file_path, "w") as file:
    file.write(required) # Print the first 1000 characters


# if response.status_code == 200:
#     # Parse the fetched HTML using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find the <ul> element with the specific class
#     ul_element = soup.find('ul', class_='H5RunningMovies_gridWrapper__H4DAC')
#     print(ul_element)
#     # List to store movie names
#     movie_names = []

#     if ul_element:
#         # Find all <script> tags with type="application/ld+json" inside this <ul>
#         for script_tag in ul_element.find_all('script', type='application/ld+json'):
#             json_data = script_tag.string
#             if json_data:
#                 # Parse JSON and extract movie name
#                 data = json.loads(json_data)
#                 if '@type' in data and data['@type'] == 'Movie' and 'name' in data:
#                     movie_names.append(data['name'])

#     # Print the extracted movie names
#     print(movie_names)
# else:
#     print(f"Failed to fetch the URL. Status code: {response.status_code}")
