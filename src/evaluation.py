# Quantitative Evaluation Metric

def calculate_filter_match_rate(recommendations, max_hours, budget):
    cost_order = {"Low": 1, "Medium": 2, "High": 3}
    matches = 0
    total = len(recommendations)

    if total == 0:
        return 100.0

    for _, row in recommendations.iterrows():
        if row["duration_hours"] <= max_hours and cost_order[row["cost_level"]] <= cost_order[budget]:
            matches += 1

    return round((matches / total) * 100.0, 1)
