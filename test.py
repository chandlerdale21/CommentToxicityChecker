from joblib import load

from predict import make_prediction  


model = load('toxic_comment_classifier.joblib')
vectorizer = load('tfidf_vectorizer.joblib')


example_comment = "you suck"


prediction = make_prediction(model, vectorizer, example_comment)

print(f"Prediction for '{example_comment}': {prediction}")