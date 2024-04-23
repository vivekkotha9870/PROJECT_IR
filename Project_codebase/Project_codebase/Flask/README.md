
# Flask NLTK Text Processor

## Overview
The Flask NLTK Text Processor is a web application that provides functionality for processing text queries. It includes features such as spelling correction, query expansion, and searching for relevant results using NLTK.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-nltk-text-processor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-nltk-text-processor
   ```
3. Install dependencies using pip:
   ```bash
   pip install Flask nltk
   ```
4. Download NLTK data (if not already downloaded):
   ```bash
   python -m nltk.downloader punkt wordnet
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Access the application in a web browser:
   ```
   http://localhost:5000
   ```
3. Enter a text query and specify the number of desired results (k).
4. Submit the query to see the corrected query, expanded query, and relevant results.

## Folder Structure
- `templates/`: Folder containing HTML templates for the web application.
- `app.py`: Flask application code for handling requests and processing queries.
- `README.md`: This file, providing instructions for running the application.

## Notes
- The application uses NLTK for text processing, including spelling correction and query expansion.
- Ensure that NLTK is properly installed and the required data is downloaded before running the application.