from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, PromptTemplate
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from movie_search import movie_search
from movie_link_getter import get_movie_link
from dotenv import load_dotenv
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

def initialize_llm():
    """Initialize the LLM with proper error handling."""
    try:
        return Ollama(
            model="llama3.2",
            request_timeout=500.0,
            temperature=0.7
        )
    except Exception as e:
        logger.error(f"Failed to initialize LLM: {str(e)}")
        raise

def setup_vector_index(llm):
    """Set up the vector index with error handling."""
    try:
        logger.info("Initializing vector index...")
        return movie_search()
    except Exception as e:
        logger.error(f"Failed to create vector index: {str(e)}")
        raise

def create_tools(query_engine):
    """Create tools for the agent."""
    return [
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name="movie_data",
                description="Search for movies available in your city, including show times and theaters"
            )
        ),
        get_movie_link
    ]

def setup_agent(llm, tools):
    """Set up the ReAct agent with proper configuration."""
    try:
        return ReActAgent.from_tools(
            tools,
            llm=llm,
            verbose=True,
            context="""You are a helpful AI assistant that helps users find information about movies.

            Dont ever make a thought by yourself of getting movie link unless the user said so.
            
            To answer questions, you'll need to:
            1. Think about what information you need
            2. Use the available tools to get that information
            3. Form a response based on the information
            
            Follow this format EXACTLY:
            Thought: I need to figure out what to do
            Action: [the action to take]
            Action Input: [the input to the action]
            Observation: [the result of the action]
            ... (repeat Thought/Action/Action Input/Observation as needed)
            Thought: I now know the final answer
            Final Answer: [your response to the human],
            """,
            max_iterations=10
        )
    except Exception as e:
        logger.error(f"Failed to create agent: {str(e)}")
        raise

def process_query(agent, query):
    """Process a single query with proper error handling."""
    try:
        return agent.query(query)
    except ValueError as e:
        if "Could not parse output" in str(e):
            logger.warning("Response parsing error. Adjusting format...")
            # You could implement retry logic here
            raise
        elif str(e) == "Reached max iterations.":
            logger.warning("Query exceeded maximum iterations")
            return "I apologize, but I couldn't find a complete answer within the allowed time. Could you try rephrasing your question?"
        else:
            logger.error(f"Unexpected ValueError: {str(e)}")
            raise
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise

def main():
    try:
        # Initialize components
        load_dotenv()
        llm = initialize_llm()
        logger.info("LLM initialized successfully")

        # Set up vector index
        vector_index = setup_vector_index(llm)
        query_engine = vector_index.as_query_engine(llm=llm)
        logger.info("Vector index and query engine created successfully")

        # Create tools and agent
        tools = create_tools(query_engine)
        agent = setup_agent(llm, tools)
        logger.info("Agent setup completed successfully")

        # Main interaction loop
        while (prompt := input("\nEnter query (q for quit): ").strip()) != "q":
            try:
                logger.info(f"Processing query: {prompt}")
                result = process_query(agent, prompt)
                print("\nResponse:", result)
            except Exception as e:
                print(f"\nError processing query: {str(e)}")
                print("Please try again with a different question.")

    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        print("\nAn error occurred while setting up the system. Please check the logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()