## Made by Gekko

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
def load_data():
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    return data, iris.target_names

# Preprocess the data
def preprocess_data(data):
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

# Train the model
def train_model(X_train, y_train):
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test, target_names):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_names)
    return accuracy, report

# Make predictions
def make_predictions(model, X_new):
    predictions = model.predict(X_new)
    return predictions

def main():
    # Load and preprocess data
    data, target_names = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Evaluate the model
    accuracy, report = evaluate_model(model, X_test, y_test, target_names)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    
    # Make predictions on new data
    X_new = np.array([[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]])  # Example new data
    predictions = make_predictions(model, X_new)
    print("Predictions for new data:")
    for i, pred in enumerate(predictions):
        print(f"Sample {i+1}: {target_names[pred]}")

if __name__ == "__main__":
    main()