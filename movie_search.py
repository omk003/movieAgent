from bs4 import BeautifulSoup
import requests
from llama_index.core import VectorStoreIndex
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core import Document

# Load your HTML data
def movie_search():

    url = "https://paytm.com/movies/aurangabad"
    response = requests.get(url)
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract text
    text_content = soup.get_text(separator="\n")  # Separate lines for better structure
    # Basic preprocessing
    cleaned_text = text_content.strip()
    # Split into smaller chunks (optional)
    max_chunk_size = 500  # Adjust size based on your use case
    text_chunks = [cleaned_text[i:i+max_chunk_size] for i in range(0, len(cleaned_text), max_chunk_size)]
    # Convert each chunk into a Document
    documents = [Document(text=chunk) for chunk in text_chunks]
    embed_model = resolve_embed_model("local:BAAI/bge-m3")
    vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    return vector_index



# get_movie_data = FunctionTool.from_defaults(
#     fn = movie_search,
#     name = "movie_list",
#     description= "Use this tool when you want to get data about movies , movies in theaters now and available movies"
# )

# result = movie_search("tell me available movies now")
# print(result)