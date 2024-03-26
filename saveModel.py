from joblib import dump

# Function to save the model to a file
def save_model(model, filename):
    dump(model, filename)

if __name__ == "__main__":
    print("Save model module loaded. Use save_model function to save your trained model.")