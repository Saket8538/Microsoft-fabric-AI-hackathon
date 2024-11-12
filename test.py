import pyodbc
import os
from dotenv import load_dotenv
import openai

load_dotenv() # Load environment variables from .env file


conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=' + os.getenv('SQL_SERVER') + ';'
    r'DATABASE=' + os.getenv('SQL_DATABASE') + ';'
    r'UID=' + os.getenv('SQL_USERNAME') + ';'
    r'PWD=' + os.getenv('SQL_PASSWORD') + ';'
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected to SQL Database")

    openai.api_key = os.getenv('OPENAI_API_KEY')


    def analyze_sentiment(review):
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose a suitable model
            prompt=f"Analyze the sentiment of this review: {review}. Return 'Positive', 'Negative', or 'Neutral'.",
            max_tokens=30,
            n=1,
            stop=None,
            temperature=0.5,
        )
        sentiment = response.choices[0].text.strip()
        return sentiment

    cursor.execute("SELECT ReviewText,ReviewID FROM CustomerReviews")
    reviews = cursor.fetchall()

    for review_tuple in reviews:
        review_text = review_tuple[0]
        review_id = review_tuple[1]
        sentiment = analyze_sentiment(review_text)
        cursor.execute("UPDATE CustomerReviews SET Sentiment = ? WHERE ReviewID = ?", sentiment, review_id)

    conn.commit()
    print("Sentiment analysis complete and database updated.")

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    if sqlstate == "28000":
        print("Authentication error. Check your connection string.")
    else:
        print(f"Error connecting to SQL Database: {ex}")
except openai.error.OpenAIError as e:
    print(f"OpenAI API error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    conn = None
    if conn:
        conn.close()
