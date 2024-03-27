To create an executable file from the above code run the following commands in order 

python -m PyInstaller --onefile --windowed --add-data "toxic_comment_classifier.joblib;." --add-data "tfidf_vectorizer.joblib;." main.py  

python -m  PyInstaller main.spec
