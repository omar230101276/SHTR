import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Popularity Baseline

def get_popularity_baseline(data, top_n=3):
    popular_ids = [1, 7, 2, 21, 3, 4, 10, 14, 15, 12]
    baseline = data[data["id"].isin(popular_ids)].copy()
    baseline["rank"] = baseline["id"].apply(popular_ids.index)
    return baseline.sort_values("rank").head(top_n)

# TF-IDF Cosine Similarity Model

def get_tfidf_recommendations(data, selected_tags, top_n=3):
    if not selected_tags:
        return get_popularity_baseline(data, top_n)

    user_text = " ".join(selected_tags)
    model_path = "models/tfidf_vectorizer.joblib"

    # Use saved model if available, else fit online
    if os.path.exists(model_path):
        vectorizer = joblib.load(model_path)
    else:
        vectorizer = TfidfVectorizer()
        vectorizer.fit(data["tags"])

    user_vector = vectorizer.transform([user_text])
    item_vectors = vectorizer.transform(data["tags"])

    scores = cosine_similarity(user_vector, item_vectors)[0]

    results = data.copy()
    results["score"] = scores
    results = results.sort_values("score", ascending=False)

    return results.drop_duplicates("category").head(top_n)
