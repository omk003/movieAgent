from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, PromptTemplate
from llama_index.core.agent import ReActAgent
from get_theaters import cinema_showtime_reader
from seats import seat_reader
from dotenv import load_dotenv
from movie_data_tool import movie_reader
from flask import Flask, request, jsonify

llm = Ollama(
            model="llama3.2",
            request_timeout=500.0,
            temperature=0.7
        )

tools = [
    movie_reader,
    cinema_showtime_reader,
    seat_reader,
]

agent = ReActAgent.from_tools(
            tools,
            llm=llm,
            verbose=True,
            context="""You are a helpful AI assistant that helps users find information about movies.
            
            To answer questions, you'll need to:
            1. Think about what information you need
            2. Use the available tools to get that information
            3. Form a response based on the information
            city name is bengaluru.

            if user asks for movie list use tool movie_reader,
            if you are ask about cinema for particular movie then use cinema_reader tool and give input of movie name,
            if you are asked about showtime by movie and cinema/theatres use the showtime_reader tool and give input movie_name and cinema.
            
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

# while (prompt := input("\nEnter query (q for quit): ").strip()) != "q":
#             try:
#                 result = agent.query(prompt)
#                 print("\nResponse:", result)
#             except Exception as e:
#                 print(f"\nError processing query: {str(e)}")
#                 print("Please try again with a different question.")


# Create a Flask app
app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_query():
  try:
    # Get the user prompt from the request body
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
      return jsonify({"error": "Missing prompt in request body"}), 400

    # Process the prompt using the agent
    result = agent.query(prompt)

    return jsonify({"response": result})

  except Exception as e:
    print(f"\nError processing query: {str(e)}")
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(debug=True)