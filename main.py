
import os

#print(completion.choices[0].message)
#
# from openai import OpenAI
# client = OpenAI(api_key="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")
#
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )
#
# print(completion.choices[0].message)


from langchain_community.utilities.sql_database import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///movie_reviews.db")

from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY"),model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

agent_executor.invoke(
    "what is this table about ?"
)





