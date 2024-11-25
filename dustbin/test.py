from duckduckgo_search import DDGS
from fpdf import FPDF
import os

# Ensure the "data" folder exists
os.makedirs('data', exist_ok=True)

def web_search(query):
    try:
        file_path = 'data/movies_data.pdf'
        results = DDGS().text(query, max_results=5)

        # Combine all results into a single text block
        text_content = ""
        for result in results:
            title = result.get('title', 'No Title')
            link = result.get('href', 'No Link')
            description = result.get('body', 'No Description')
            text_content += f"Title: {title}\nLink: {link}\nDescription: {description}\n\n"

        # Create a PDF and add the text
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text_content)  # Add the full text to the PDF

        # Save the PDF
        pdf.output(file_path)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        return {"error": str(e)}

web_search("which sites from i can book movies?")
