from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random as rd
import os
from time import time

app = Flask(__name__)

# Backend (Server-side) to process the request

#For formatting of the dataset
def clean(fln):
    """Load movie dataset from CSV."""
    try:
        df = pd.read_csv(fln)
        df.rename(columns={'overview': 'description'}, inplace=True)
        df = df[['title', 'description']].dropna()
        df['title'] = df['title'].str.strip().str.lower()  # Normalize titles

        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame(columns=['title', 'description'])

fln = os.path.join(os.getcwd(), 'mysite', 'movies.csv')
movie_df = clean(fln)

# Cosine similarity algorithm to recommend movie based on user input
def recommend_movies(user_input, top_n=5):
    """Recommend top N movies based on text similarity."""
    if movie_df.empty:
        return [], 0  # Return empty list and zero time

    texts = [user_input] + movie_df['description'].tolist()

    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(texts)

    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]

    top_indices = similarities.argsort()[-top_n:][::-1]

    return movie_df.iloc[top_indices][['title', 'description']].to_dict(orient='records')

# Server request protocol
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("movie_desc", "").strip()
        if user_input:
            start_time = time()
            recommendations = recommend_movies(user_input, rd.randint(3,5))
            elapsed_time = time() - start_time
            return render_template("index.html", recommendations=recommendations, elapsed_time=elapsed_time, user_input=user_input)

    # If it's a GET request (page visit), don't process anything, just show the form
    return render_template("index.html", recommendations=None, elapsed_time=None, user_input="")

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
