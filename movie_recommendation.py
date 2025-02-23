from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function for the cosine similarity algorithm to recommend the movies based on user input: Used by the CLI & GUI
def recommend(user_input, movie_df, top_n=5, gui=False):
    """Recommend top N movies based on text similarity."""
    # Combine user input with movie descriptions
    texts = movie_df['Description'].tolist()
    texts.insert(0, user_input)  # Insert user input at the beginning
    
    # Convert text data into TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Compute cosine similarity between user input and movie descriptions
    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]
    
    # Get top N similar movies
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    result = movie_df.iloc[top_indices][['Title', 'Description']]
    
    #T To handle CLI or GUI request
    if not(gui):
        result = result.reset_index(drop=True)
        result.insert(0, 'S/No.', range(1, len(result) + 1))
        result = result.reset_index(drop=True)
        
    else:
        result = movie_df.iloc[top_indices][['Title', 'Description']].copy()
        result.insert(0, 'ID', range(1, len(result) + 1))
    
    # Return recommended movies
    return result