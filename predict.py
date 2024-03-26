def make_prediction(model, vectorizer, new_comment):
    new_comment_vectorized = vectorizer.transform([new_comment])
    prediction = model.predict(new_comment_vectorized)
    return prediction

if __name__ == "__main__":
    print("Prediction module loaded. Use make_prediction function to make new predictions.")