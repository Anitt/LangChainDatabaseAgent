import os
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

class LangchainAgent:
    def __init__(self):
        try:
            db = SQLDatabase.from_uri("sqlite:///database/movie_reviews.db")
            self.llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"), model="gpt-3.5-turbo", temperature=0)
            self.agent_executor = create_sql_agent(self.llm, db=db, agent_type="openai-tools", verbose=True)
        except Exception as e:
            raise Exception(f"Error initializing LangchainAgent: {str(e)}")

    def get_response(self, user_query):
        try:
            response = self.agent_executor.invoke(user_query)
            return response  # Return the raw response
        except Exception as e:
            return f"Error: {str(e)}"
