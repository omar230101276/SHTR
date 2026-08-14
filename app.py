import streamlit as st
from src.data_processing import load_data, apply_hard_filters
from src.model import get_tfidf_recommendations, get_popularity_baseline
from src.evaluation import calculate_filter_match_rate

# Load Dataset
df = load_data()

# App Header
st.title("Smart Heritage Tourism Recommender")

# Sidebar Filters
st.sidebar.header("Hard Filters")

location = st.sidebar.selectbox("Location", ["All", "Cairo", "Giza"])
budget = st.sidebar.selectbox("Budget", ["Low", "Medium", "High"])
hours = st.sidebar.selectbox("Available Hours", [1, 2, 3, 4], index=3)
period = st.sidebar.selectbox("Visit Period", ["Full Day", "Morning", "Evening"])
wheelchair = st.sidebar.checkbox("Wheelchair Accessible")

# User Interests Input
tags = ["history", "ancient", "monuments", "museum", "shopping",
        "culture", "nature", "views", "architecture", "religion",
        "art", "music", "garden"]

selected_tags = st.multiselect("Choose your interests", tags)

# Main Recommendation Loop
if st.button("Get Recommendations"):

    # Apply Hard Filters
    filtered_data = apply_hard_filters(df, location=location, budget=budget,
                                       hours=hours, period=period, wheelchair=wheelchair)

    if filtered_data.empty:
        st.warning("No places match your choices.")

    elif not selected_tags:
        st.subheader("Popularity Baseline")
        baseline = get_popularity_baseline(filtered_data)

        for _, row in baseline.iterrows():
            st.write(f"📍 {row['name']} | {row['location']} | "
                     f"{row['duration_hours']} hours | {row['cost_level']}")

        metric = calculate_filter_match_rate(baseline, hours, budget)
        st.metric(label="Filter Match Rate", value=f"{metric}%")

    else:
        # TF-IDF Cosine Similarity Recommendation
        results = get_tfidf_recommendations(filtered_data, selected_tags)

        st.subheader("Top 3 Recommendations")

        for _, row in results.iterrows():
            st.write(f"### 📍 {row['name']}")
            st.write(f"Category: {row['category']}")
            st.write(f"Location: {row['location']}")
            st.write(f"Duration: {row['duration_hours']} hours")
            st.write(f"Cost: {row['cost_level']}")
            st.write(f"Similarity: {round(row['score'] * 100, 1)}%")
            st.write("Reason: This place matches your interests and filters.")

        # Metric Display
        metric = calculate_filter_match_rate(results, hours, budget)
        st.metric(label="Filter Match Rate", value=f"{metric}%")

        # Baseline Comparison
        st.subheader("Popularity Baseline Comparison")
        baseline = get_popularity_baseline(filtered_data)

        for _, row in baseline.iterrows():
            st.write(f"• {row['name']} ({row['category']})")