import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Dataset

def train_and_save_model():
    print("Loading dataset...")
    df = pd.read_csv("data/raw/egypt_attractions.csv")

    # Fit TF-IDF Vectorizer
    print("Fitting TF-IDF Vectorizer on attraction tags...")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["tags"])

    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)

    # Save Model Artifacts
    print("Saving model artifacts to models/ directory...")
    joblib.dump(vectorizer, "models/tfidf_vectorizer.joblib")
    joblib.dump(tfidf_matrix, "models/tfidf_matrix.joblib")

    print("Model training complete! Saved artifacts:")
    print(" - models/tfidf_vectorizer.joblib")
    print(" - models/tfidf_matrix.joblib")

if __name__ == "__main__":
    train_and_save_model()
