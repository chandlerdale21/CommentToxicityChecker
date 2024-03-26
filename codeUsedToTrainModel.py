from loadDataset import load_and_vectorize_data
from trainModel import train_model
from predict import make_prediction
from saveModel import save_model


def main():
    
    X, y, vectorizer = load_and_vectorize_data('train.csv')
    

    model = train_model(X, y)
    
   
    save_model(model, 'toxic_comment_classifier.joblib')
    save_model(vectorizer, 'tfidf_vectorizer.joblib')

    
    example_comment = "This is a test"
    prediction = make_prediction(model, vectorizer, example_comment)
    print(f"Predicted categories: {prediction}")

if __name__ == "__main__":
    main()