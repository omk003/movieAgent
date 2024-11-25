from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader, 
    PromptTemplate
)
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from prompts import context
from dustbin.movie_link_getter import get_movie_link
from dotenv import load_dotenv

load_dotenv()

def initialize_system():
    llm = Ollama(
        model="llama3.2",
        request_timeout=250.0
    )
    
    # parser = LlamaParse(
    #     result_type="markdown"
    # )
    
    return llm#, parser

# def create_index(llm, parser):
#     # Configure file extraction
#     file_extractor = {".pdf": parser}
    
#     # Load documents with correct parameters
#     # documents = SimpleDirectoryReader(
#     #     input_dir="./data",  # Changed from "./data" to input_dir="./data"
#     #     file_extractor=file_extractor
#     # ).load_data()
    
#     # Initialize embedding model
#     #embed_model = resolve_embed_model("local:BAAI/bge-m3")
    
#     # Create vector index
#     #vector_index = VectorStoreIndex.from_documents(
#     #    documents,
#     #    embed_model=embed_model
#     #)
    
#     return vector_index

def setup_agent(llm):
    #query_engine = vector_index.as_query_engine(llm=llm)
    
    tools = [
        get_movie_link,
    ]
    
    agent = ReActAgent.from_tools(
        tools,
        llm=llm,
        verbose=True,
        context=context,
        max_iterations=10
    )
    
    return agent

def main():
    llm = initialize_system()
    #vector_index = create_index(llm, parser)
    agent = setup_agent(llm)
    
    while (prompt := input("Enter: (q for quit): ")) != "q":
        try:
            result = agent.query(prompt)
            print(result)
        except ValueError as e:
            if str(e) == "Reached max iterations.":
                print("Query resolution timeout. Please try a simpler query.")
            else:
                print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()