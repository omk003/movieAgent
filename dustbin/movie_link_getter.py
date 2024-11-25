from llama_index.core.tools import FunctionTool
from bs4 import BeautifulSoup
import requests
from llama_index.core import Document
import regex as re
    


# Optimized function to get a movie link
def get_movie_link_fun(movie_name):
    def movie_link_fun():
        # Create a dictionary to store movie names and their corresponding links
        def build_movie_index(documents):
            movie_index = {}
            for doc in documents:
                doc_text = doc.get_text()
                lines = doc_text.split("\n")
                movie_name = lines[0].replace("Movie Name: ", "").strip()
                link = lines[1].replace("Book Ticket Link: ", "").strip()
                movie_index[movie_name.lower()] = link  # Use lowercase for case-insensitive lookup
            return movie_index
        try:
            url = "https://paytm.com/movies/aurangabad"
            # Fetch the HTML content from the URL
            response = requests.get(url)
            required = response.text[22000:45000] 
            soup = BeautifulSoup(required, "html.parser")
            base_url = "https://paytm.com"

            # Extract links and generate documents
            documents = []
            for tag in soup.find_all('a', href=True, string="Book Ticket"):
                link = base_url + tag['href']
                movie_name_raw = link.split("/")[-1].replace("-movie-detail-", " ").replace("-", " ").title()
                movie_name = re.sub(r"\d+$", "", movie_name_raw).strip()
                document_text = f"Movie Name: {movie_name}\nBook Ticket Link: {link}"
                documents.append(Document(text=document_text))
            return build_movie_index(documents)


        except Exception as e:
            return {"error": str(e)}
    movie_index = movie_link_fun()
    return {"movie_link": movie_index.get(movie_name.lower(), "Movie link not found.")}


get_movie_link = FunctionTool.from_defaults(
    fn = get_movie_link_fun,
    name = "movie_link",
    description= "Use this tool when you want to get a link for movie ticket book by name. Dont use this tool unless you want link of movie"
)


