import pandas as pd

# Load Dataset

def load_data(filepath="data/raw/egypt_attractions.csv"):
    return pd.read_csv(filepath)

# Apply Hard Filters

def apply_hard_filters(df, location="All", budget="High", hours=4, period="Full Day", wheelchair=False):
    data = df.copy()

    # Location Filter
    if location != "All":
        data = data[data["location"] == location]

    # Wheelchair Accessibility Filter
    if wheelchair:
        data = data[data["wheelchair_accessible"] == "Yes"]

    # Visit Period Filter
    if period != "Full Day":
        data = data[(data["opening_period"] == period) | (data["opening_period"] == "Full Day")]

    # Budget and Available Hours Filter
    cost_order = {"Low": 1, "Medium": 2, "High": 3}
    data = data[(data["cost_level"].map(cost_order) <= cost_order[budget]) & (data["duration_hours"] <= hours)]

    return data
