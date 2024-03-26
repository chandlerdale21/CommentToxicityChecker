from joblib import load
# Adjust the import path if your make_prediction function is located elsewhere
from predict import make_prediction  

# Load your saved model and vectorizer
model = load('toxic_comment_classifier.joblib')
vectorizer = load('tfidf_vectorizer.joblib')

# Example comment to classify
example_comment = "you suck"

# Call make_prediction with the loaded model, vectorizer, and your example comment
prediction = make_prediction(model, vectorizer, example_comment)

# Print the prediction to see if it's working as expected
print(f"Prediction for '{example_comment}': {prediction}")