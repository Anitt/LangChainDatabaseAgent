from datasets import load_dataset
import sqlite3

# Load dataset from Hugging Face
dataset = load_dataset("imdb")

# SQLite database connection
conn = sqlite3.connect('movie_reviews.db')
cursor = conn.cursor()

# Create table for movie reviews
cursor.execute('''CREATE TABLE movie_reviews
                (review TEXT, label TEXT)''')

# Insert data into SQLite table
for example in dataset['train']:
    cursor.execute('''INSERT INTO movie_reviews (review, label)
                      VALUES (?, ?)''', (example['text'], example['label']))

# Commit changes and close connection
conn.commit()
conn.close()

print("SQLite database 'movie_reviews.db' created and populated.")
