import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to load and vectorize the dataset
def load_and_vectorize_data(filepath):
    df = pd.read_csv(filepath)
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    X_tfidf = tfidf_vectorizer.fit_transform(df['comment_text'])
    y = df[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']]
    return X_tfidf, y, tfidf_vectorizer

if __name__ == "__main__":
    # Test the loading function
    X, y, vectorizer = load_and_vectorize_data('train.csv')
    print("Dataset loaded and vectorized.")