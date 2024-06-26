# LangChain Database Agent

This project is a web-based application that uses the Langchain RAG framework with OpenAI to respond to natural language queries directed at an SQLite database. The application leverages Flask for the backend and provides an interactive interface for users.

## Features

- Interactive web interface for natural language input.
- Processes user queries and interacts with an SQLite database.
- Utilizes the Langchain RAG framework with OpenAI for intelligent responses.
- Scalable and customizable for different use cases involving natural language and databases.

## Prerequisites

- Python 3.9 or higher
- Flask
- OpenAI API Key
- Langchain
- SQLite3
- Gradio

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/LangChainDatabaseAgent.git
   cd LangChainDatabaseAgent
2. ## Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. ## Install the required packages:

    pip install -r requirements.txt

4. ## Set up the environment variables:

   OPENAI_API_KEY=your-openai-api-key


## Usage

1. ## Run the Flask application:

     flask run
   
2. ## Open your web browser and go to http://127.0.0.1:5000 to access the web application.

## File Structure

1.app.py: The Flask application file that handles API requests and serves the web application.

2.agent.py: This file contains the Langchain Agents used to interface between OpenAI and the SQL database.

3.index.html: The main HTML file located in the templates directory, responsible for the user interface layout.

4.routes.py: Defines the routes and logic for handling different API endpoints in the Flask application.

5.database.db: The SQLite database file storing the movie reviews and labels.

6.templates/: Directory containing additional HTML templates for the web interface.

7.requirements.txt: List of required Python packages necessary to run the application.


## How It Works
1.The user inputs their query in natural language through the web interface.

2.The query is sent to the Flask backend via a POST request.

3.The backend processes the input using the Langchain RAG framework - Agent with OpenAI.

4.The processed query interacts with the SQLite database to fetch the relevant information.

5.The response is returned to the user and displayed on the web interface.

## Screenshots

![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/b6a2655f-66ff-410f-9079-ed7c85243441)


![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/f0a87868-be99-4194-a933-029148b553c5)

# Gradio Interface Screenshots

![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/401e55ca-a23d-403b-a618-e958be33b0f2)


![image](https://github.com/Anitt/LangChainDatabaseAgent/assets/32222717/03d868b6-45b9-4bbf-8e40-ddeac8ef58f4)





   
