from joblib import load
from gui import start_gui

def main():
    # Load the trained model and vectorizer
    model = load('toxic_comment_classifier.joblib')
    vectorizer = load('tfidf_vectorizer.joblib')

    # Start the GUI and pass the model and vectorizer to it
    start_gui(model, vectorizer)

if __name__ == "__main__":
    main()