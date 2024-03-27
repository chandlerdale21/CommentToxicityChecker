import os
import sys
from joblib import load
from gui import start_gui

def get_resource_path(relative_path):
    """ Get the absolute path to the resource, works for development and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    # Use get_resource_path to ensure the paths are correct when bundled by PyInstaller
    model_path = get_resource_path('toxic_comment_classifier.joblib')
    vectorizer_path = get_resource_path('tfidf_vectorizer.joblib')

    # Load your model and vectorizer using the adjusted paths
    model = load(model_path)
    vectorizer = load(vectorizer_path)

    # Start the GUI and pass the model and vectorizer
    start_gui(model, vectorizer)

if __name__ == "__main__":
    main()