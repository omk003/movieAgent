Welcome to the Hands-On Guide of Lunar-Bot by TeamUI
Lunar-Bot is a cutting-edge tool designed to scrape live data from Paytm Movies, providing real-time updates on currently screening movies. Whether it's the availability of seats, theatre names, show timings, or seat types, Lunar-Bot has you covered—all without relying on any third-party APIs, ensuring a fully independent structure.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Tech Stack***
Llama3.2: The backbone for efficient data embedding and query processing.
Llama-Index: Enables advanced indexing and querying for seamless information retrieval.
Frontend: Built using HTML, JS, and CSS for a clean and user-friendly interface.
Backend: Powered by Flask, ensuring robust and scalable server-side logic.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Features***
Real-Time Updates
Lunar-Bot fetches live data directly from Paytm Movies, keeping you up-to-date with:
Currently Screening Movies.
Show Timings.
Theatre Names.
Seat Availability and Types.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Independence from APIs
By bypassing third-party APIs, Lunar-Bot creates an independent ecosystem with greater flexibility and reliability.
**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Powered by Advanced AI
  With Llama3.2, Lunar-Bot achieves:
  High Accuracy: Extracts relevant details efficiently.
  Optimal Speed: Processes large datasets with minimal lag.
  First-Time Use Delays
  While the embedding model may take some time to initialize during the first run, subsequent usage is significantly faster.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Deployment Guide
To deploy Lunar-Bot and get it running, follow these steps:
  1. Setup the Environment
    Create a virtual environment in your local system:
            python -m venv lunarbot-env
   Activate the virtual environment:
    On Windows:
            lunarbot-env\Scripts\activate
    On macOS/Linux:
            source lunarbot-env/bin/activate
  2. Install Requirements
    Navigate to the project directory and install the necessary dependencies:
            pip install -r requirements.txt
  3. Run the Application
    Execute the main script to start Lunar-Bot:
            python run.py
  4. Initial Embedding Setup
    The first execution may take additional time to embed the Llama model and index data. Please be patient as this is a one-time setup.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Expected Output
Once deployed successfully, Lunar-Bot provides a clean and detailed list of movie details, including:

  Theatre Names: A comprehensive list of theatres screening the movies.
  Showtimes: Accurate and up-to-date timings for each show.
  Movie Titles: Names of the movies currently screening.
  Seat Information:
  Number of seats available.
  Types of seats (e.g., Regular, VIP).
  Known Issues and Future Fixes
**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#While Lunar-Bot is highly reliable, deployment has highlighted a few minor issues:
Embedding Delays: As mentioned earlier, the first-time loading of models may take time but can be optimized in future iterations.
UI Improvements: Enhancing the frontend for a more intuitive user experience.
Additional Features: Adding filters for specific genres, price ranges, or languages.
These issues are easily fixable and will be addressed in subsequent updates.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
_Why Lunar-Bot?
Lunar-Bot is the perfect tool for users looking for real-time, independent movie show updates without relying on external APIs. Its robust architecture, powered by Llama3.2, ensures reliability, accuracy, and independence.
Get ready to explore the world of live movie data scraping with Lunar-Bot! 🚀_
