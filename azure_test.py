from llama_index.readers.json import JSONReader
from llama_index.core import VectorStoreIndex
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.llms.ollama import Ollama
#from llama_index import StorageContext

llm = Ollama(
            model="llama3.2",
            request_timeout=500.0,
            temperature=0.7
        )
# Configure Azure OpenAI GPT-4
# consuming too much tokens and not working on current tier of account
# llm = AzureOpenAI(
#     engine="gpt-4", 
#     model="gpt-4", 
#     azure_endpoint="https://onkar-m3w3rptk-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-08-01-preview", 
#     api_key="################################################",  
#     api_version="2024-10-21", 
#     temperature=0.7,
#     max_tokens=220,  # Adjust as needed
# )
# Use OpenAI's embedding model via Azure
# embed_model_live = AzureOpenAIEmbedding(
#     engine = "text-embedding-ada-002",
#     deployment_name="text-embedding-ada-002",
#     model="text-embedding-ada-002", 
#     azure_endpoint="https://onkar-m3w3rptk-eastus2.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15",
#     api_key="######################################################################",
#     api_version="2024-10-01-preview",
    
# )

# rebuild storage context
#storage_context = StorageContext.from_defaults(persist_dir="./storage")

reader = JSONReader(levels_back=7)
documents = reader.load_data("movies_data.json")
embed_model = resolve_embed_model("local:BAAI/bge-m3")
index = VectorStoreIndex.from_documents(documents,embed_model=embed_model)
# load index
#index = load_index_from_storage(storage_context, embed_model=embed_model)

# Create a query engine    
query_engine = index.as_query_engine(llm=llm)

tools = [
       QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name="movie_data",
                description="use this tool when you want to know about movies ,theatres"
            )
        ),
]
agent = ReActAgent.from_tools(
            tools,
            llm=llm,
            verbose=True,
            context="""you are a helpful ai assitant ,
            user will only ask about movies,theaters , and there showtimes
            so answer them using the tools
            """,
            max_iterations=6
        )

res = query_engine.query("give me movies available ")
print(res)

# Load the JSON data
# reader = JSONReader(levels_back=7)
# documents = reader.load_data("movies_data.json")

# Use a compatible embedding model
#embed_model = resolve_embed_model(embed_model_live)

# Create a vector store index
#index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

#index.save_to_disk("vector_index.json")
# Save index
# storage_context = index.storage_context
# storage_context.persist(persist_dir="./storage")


# while (prompt := input("\nEnter query (q for quit): ").strip()) != "q":
#             try:
#                 result = agent.query(prompt)
#                 print("\nResponse:", result)
#             except Exception as e:
#                 print(f"\nError processing query: {str(e)}")
#                 print("Please try again with a different question.")



# # Example query
# response = query_engine.query("What are the showtimes for Bhool Bhulaiyaa 3?")
# print(response)