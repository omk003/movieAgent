from llama_index.core import VectorStoreIndex
from llama_index.readers.web import BeautifulSoupWebReader
from llama_index.llms.ollama import Ollama
from llama_index.core.embeddings import resolve_embed_model



def movie_search_new():
    # Initialize the BeautifulSoupWebReader
    reader = BeautifulSoupWebReader()

    llm = Ollama(model="llama3.2", request_timeout=300.0)
    # List of URLs to scrape
    urls = ["https://paytm.com/movies/aurangabad"]

    # Load data from the URLs
    documents = reader.load_data(urls=urls)
    embed_model = resolve_embed_model("local:BAAI/bge-m3")
    # Create an index from the documents
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

    # Create a query engine
    #query_engine = index.as_query_engine(llm=llm)
    return index


# while (prompt := input("\nEnter query (q for quit): ").strip()) != "q":
#             try:
#                 result = query_engine.query(prompt)
#                 print("\nResponse:", result)
#             except Exception as e:
#                 print(f"\nError processing query: {str(e)}")
#                 print("Please try again with a different question.")
# Ask a question
