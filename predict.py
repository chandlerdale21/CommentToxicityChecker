def make_prediction_with_confidence(model, vectorizer, new_comment):
    new_comment_vectorized = vectorizer.transform([new_comment])
    # Get confidence scores (probabilities) for each output
    confidence_scores = model.predict_proba(new_comment_vectorized)
    
    # Calculate the average of the maximum probabilities across all outputs
    # This assumes confidence_scores is a list of arrays
    max_confidences = [output.max() for output in confidence_scores]
    avg_max_confidence = sum(max_confidences) / len(max_confidences)
    
    prediction = model.predict(new_comment_vectorized)
    return prediction, avg_max_confidence