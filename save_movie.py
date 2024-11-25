from llama_index.readers.json import JSONReader
from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core import StorageContext, load_index_from_storage

llm = Ollama(
            model="llama3.2",
            request_timeout=500.0,
            temperature=0.7
        )


# Load the JSON data / only when doing embedding
#reader = JSONReader(levels_back=7)
#documents = reader.load_data("movies_data.json")
embed_model = resolve_embed_model("local:BAAI/bge-m3")
# Create a vector store index
#index = VectorStoreIndex.from_documents(documents,embed_model=embed_model)

#for storing the data
# storage_context = index.storage_context
# storage_context.persist(persist_dir="./storage")

#for retreving the index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context, embed_model=embed_model)

query_engine = index.as_query_engine(llm=llm)


# result = query_engine.query("tell me details about movies in cinema now in bengaluru")
# print(result)
# print("end : /n")



while (prompt := input("\nEnter query (q for quit): ").strip()) != "q":
            try:
                result = query_engine.query(prompt)
                print("\nResponse:", result)
            except Exception as e:
                print(f"\nError processing query: {str(e)}")
                print("Please try again with a different question.")
# result = query_engine.query("give me details about showtimes and theatres for movie singham again in city pune")
# print(result)
# print("end : /n")
# result = query_engine.query("tell me details about seat types with availibilty of seats for movie Raanti in city aurangabad ")
# print(result)
# print("end : /n")
# result = query_engine.query("give me all movies present in city aurangabad")
# print(result)
# print("end : /n")
