import streamlit as st
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import openai


# Load environment variables
load_dotenv()

# Database connection (replace with your credentials)
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=' + os.getenv('SQL_SERVER') + ';'
    r'DATABASE=' + os.getenv('SQL_DATABASE') + ';'
    r'UID=' + os.getenv('SQL_USERNAME') + ';'
    r'PWD=' + os.getenv('SQL_PASSWORD') + ';'
)

openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_sentiment(review):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=f"Analyze the sentiment of this review: {review}. Return 'Positive', 'Negative', or 'Neutral'.",
        max_tokens=30,
        n=1,
        stop=None,
        temperature=0.5,
    )
    sentiment = response.choices[0].text.strip()
    return sentiment


try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    st.title("Customer Review Sentiment Analysis")

    # Fetch data from the database
    cursor.execute("SELECT ReviewText, Sentiment FROM CustomerReviews")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["ReviewText", "Sentiment"])

    # Display raw data (optional)
    if st.checkbox("Show Raw Data"):
        st.write(df)

    # Sentiment distribution
    sentiment_counts = df['Sentiment'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    #Example of adding a new review:
    new_review = st.text_input("Enter a new review:")
    if st.button("Analyze Review"):
        if new_review:
            new_sentiment = analyze_sentiment(new_review)
            st.write(f"Sentiment: {new_sentiment}")
            cursor.execute("INSERT INTO CustomerReviews (ReviewText,Sentiment) Values (?,?)", new_review, new_sentiment)
            conn.commit()
            st.success("Review added and analyzed!")


except pyodbc.Error as ex:
    st.error(f"Database error: {ex}")
except openai.error.OpenAIError as e:
    st.error(f"OpenAI API error: {e}")
except Exception as e:
    st.exception(e)  # Show detailed error information

finally:
    if conn:
        conn.close()