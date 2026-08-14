# Test Plan and Test Report (Appendix C)

**System Under Test**: Smart Heritage Tourism Recommender (SHTR v1.0)  
**Test Environment**: Python 3.12, Streamlit 1.61, Windows 11  
**Dataset**: `data/raw/egypt_attractions.csv` (40 attractions)  
**Acceptance Rule**: 100% Filter Match Rate for active hard constraints.  

---

## 1. Quantitative Evaluation Metric

We evaluate recommendation quality and constraint satisfaction using **Filter Match Rate**:

$$\text{Filter Match Rate} = \left( \frac{\text{Recommendations satisfying all active hard filters}}{\text{Total recommendations returned}} \right) \times 100\%$$

- **Target**: 100% (Hard filters for budget, max hours, location, and accessibility must never be violated).

---

## 2. Test Case Record (8 Required Cases)

| ID | Test Scenario | Input Criteria | Expected System Behavior | Status | Verification Method |
|---|---|---|---|---|---|
| **TC-01** | Normal recommendation | Cairo, High budget, Max 4h, History + Museum | Returns Top 3 matching Cairo places sorted by similarity | **PASS** | Automated (`test_tc01_normal_recommendation`) |
| **TC-02** | Low budget constraint | Low budget, Max 2 hours | Only returns places with `cost_level` = Low and `duration_hours` <= 2 | **PASS** | Automated (`test_tc02_low_budget`) |
| **TC-03** | Location filter | Giza location selected | Only returns places with `location` = Giza | **PASS** | Automated (`test_tc03_giza_location`) |
| **TC-04** | Wheelchair accessibility | Wheelchair = Yes | Only returns places with `wheelchair_accessible` = Yes | **PASS** | Automated (`test_tc04_wheelchair_filter`) |
| **TC-05** | Morning visit period | Morning period, Max 3 hours | Only returns places open during `Morning` or `Full Day` | **PASS** | Automated (`test_tc05_morning_visit`) |
| **TC-06** | No interests selected | No tags checked | System falls back to Popularity Baseline ranking | **PASS** | Automated (`test_tc06_no_interests_baseline`) |
| **TC-07** | No matching results | Contradictory/Strict filters | Displays user warning ("No places match your choices") | **PASS** | Automated (`test_tc07_no_matching_results`) |
| **TC-08** | Different interest tags | Nature + Views | Results are ranked dynamically by TF-IDF Cosine Similarity score | **PASS** | Automated (`test_tc08_different_interests`) |

---

## 3. User Personas Tested

1. **Persona A (History Enthusiast)**: High budget, 4 hours available in Cairo, interested in history and museums.
2. **Persona B (Budget & Accessibility Focused)**: Low budget, needs wheelchair access, 2 hours available.
3. **Persona C (Casual Explorer)**: No specific interest tags, looking for top popular attractions in Giza.
4. **Persona D (Morning Sightseer)**: Available only during morning hours for 3-hour tours.
5. **Persona E (Nature Lover)**: Low budget, interested in parks, views, and relaxation.

---

## 4. Test Execution Summary

- **Total Test Cases**: 8 (plus 1 metric verification test)
- **Passed**: 9
- **Failed**: 0
- **Automated Test Script**: `tests/test_recommender.py`
- **Result**: All test cases passed with a **100.0% Filter Match Rate**.