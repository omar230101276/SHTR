import unittest
import pandas as pd
from src.data_processing import load_data, apply_hard_filters
from src.model import get_tfidf_recommendations, get_popularity_baseline
from src.evaluation import calculate_filter_match_rate

class TestRecommender(unittest.TestCase):

    def setUp(self):
        self.df = load_data("data/raw/egypt_attractions.csv")

    # TC-01: Normal recommendation
    def test_tc01_normal_recommendation(self):
        filtered = apply_hard_filters(self.df, location="Cairo", budget="High", hours=4)
        recs = get_tfidf_recommendations(filtered, ["history", "museum"])
        self.assertGreater(len(recs), 0)

    # TC-02: Low budget
    def test_tc02_low_budget(self):
        filtered = apply_hard_filters(self.df, budget="Low", hours=2)
        cost_order = {"Low": 1, "Medium": 2, "High": 3}
        for _, row in filtered.iterrows():
            self.assertLessEqual(cost_order[row["cost_level"]], 1)
            self.assertLessEqual(row["duration_hours"], 2)

    # TC-03: Location filter
    def test_tc03_giza_location(self):
        filtered = apply_hard_filters(self.df, location="Giza")
        self.assertTrue(all(filtered["location"] == "Giza"))

    # TC-04: Wheelchair filter
    def test_tc04_wheelchair_filter(self):
        filtered = apply_hard_filters(self.df, wheelchair=True)
        self.assertTrue(all(filtered["wheelchair_accessible"] == "Yes"))

    # TC-05: Morning visit
    def test_tc05_morning_visit(self):
        filtered = apply_hard_filters(self.df, period="Morning", hours=3)
        for _, row in filtered.iterrows():
            self.assertIn(row["opening_period"], ["Morning", "Full Day"])
            self.assertLessEqual(row["duration_hours"], 3)

    # TC-06: No interests
    def test_tc06_no_interests_baseline(self):
        filtered = apply_hard_filters(self.df)
        baseline = get_popularity_baseline(filtered)
        self.assertGreater(len(baseline), 0)

    # TC-07: No matching results
    def test_tc07_no_matching_results(self):
        filtered = apply_hard_filters(self.df, location="Giza", budget="Low", hours=1, wheelchair=True)
        self.assertEqual(len(filtered), 0)

    # TC-08: Different interests
    def test_tc08_different_interests(self):
        filtered = apply_hard_filters(self.df)
        recs = get_tfidf_recommendations(filtered, ["nature", "views"])
        self.assertGreater(len(recs), 0)

    # Metric evaluation check
    def test_filter_match_rate(self):
        filtered = apply_hard_filters(self.df, budget="Medium", hours=3)
        recs = get_tfidf_recommendations(filtered, ["history"])
        rate = calculate_filter_match_rate(recs, 3, "Medium")
        self.assertEqual(rate, 100.0)

if __name__ == "__main__":
    unittest.main()
