from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from loadDataset import load_and_vectorize_data


def train_model(X, y):
    model = MultiOutputClassifier(LogisticRegression(solver='liblinear'))
    model.fit(X, y)
    return model

if __name__ == "__main__":
    X, y, _ = load_and_vectorize_data('train.csv')
    model = train_model(X, y)
    print("Model trained.")