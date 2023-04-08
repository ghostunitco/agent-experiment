import os
import psycopg2
import openai_secret_manager

# Get the PostgreSQL credentials from the secrets manager
assert "postgresql" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("postgresql")

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=secrets["dbname"],
    user=secrets["username"],
    password=secrets["password"],
    host=secrets["host"],
    port=secrets["port"],
)

# Create the tables in the database
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id SERIAL PRIMARY KEY,
    input_text TEXT NOT NULL,
    response_text TEXT NOT NULL
)
""")
conn.commit()
cur.close()
conn.close()

print("Database initialized successfully.")
