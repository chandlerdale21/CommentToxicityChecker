from joblib import load
from gui import start_gui

def main():
   
    model = load('toxic_comment_classifier.joblib')
    vectorizer = load('tfidf_vectorizer.joblib')

   
    start_gui(model, vectorizer)

if __name__ == "__main__":
    main()