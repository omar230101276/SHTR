# Live Demo Presentation Deck (Appendix E Standard)

**Course**: CET 251 Artificial Intelligence  
**Project**: Smart Heritage Tourism Recommender (SHTR - Brief D4)  
**Instructor**: Dr. Mohamed Aly Saleh  
**Presentation Time**: 5–7 Minutes  
**Slide Count**: 8 Slides  

---

## Slide 1: Title & Team Overview
- **Project Title**: Smart Heritage Tourism Recommender (SHTR)
- **Track**: Tourism & Heritage
- **Objective**: An intelligent prototype helping visitors discover tailored heritage attractions in Cairo & Giza based on hard constraints and interest preferences.
- **Team Roles**:
  - **AI/Data Lead**: Dataset curation, TF-IDF model implementation.
  - **Application Lead**: Streamlit frontend & backend integration.
  - **Testing & QA Lead**: Test plan execution & metric evaluation.
  - **Documentation Lead**: Technical report, README, and presentation.

---

## Slide 2: Problem Statement & Target Users
- **Problem**: Visitors face information overload and struggle to find attractions matching their strict budget, time limits, or accessibility requirements.
- **Target Users**:
  - History & culture tourists seeking personalized itineraries.
  - Budget-conscious travelers and students.
  - Visitors requiring wheelchair accessible sites.

---

## Slide 3: Dataset & Hard Constraint Engine (CSP Concept)
- **Dataset**: 40 curated sites across Cairo & Giza with 10 attributes (`cost_level`, `duration_hours`, `location`, `wheelchair_accessible`, `tags`).
- **Constraint Satisfaction (CSP)**:
  - Hard filters eliminate non-viable attractions prior to AI scoring.
  - Filters: Budget $\le$ User Budget, Duration $\le$ User Available Hours, Location matching, Wheelchair access check.

---

## Slide 4: AI Methodology vs Popularity Baseline
- **AI Core Method**: Content-Based Recommendation using **TF-IDF Vectorization & Cosine Similarity**.
  $$\text{Similarity}(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$
- **Baseline Comparison**: Rule-Based **Popularity Baseline** ranking top famous heritage sites (`popular_ids`).
- **Why TF-IDF?**: Interpretable, fast, requires no user history (cold-start friendly), and runs offline without paid API costs.

---

## Slide 5: System Architecture & Data Flow
- **Data Flow**:
  1. `egypt_attractions.csv` $\rightarrow$ `src/data_processing.py` (Hard Filtering)
  2. Candidate Subset $\rightarrow$ `src/model.py` (TF-IDF Vectorizer + Cosine Similarity)
  3. Ranked Recommendations + Metrics $\rightarrow$ `app.py` (Streamlit UI)

---

## Slide 6: Quantitative Evaluation & Test Results
- **Metric**: **Filter Match Rate** = 100% across all queries.
- **Testing Results**:
  - 8 Required Test Cases executed (Normal, Edge Cases, Baseline Fallback, Strict Filters).
  - 9/9 Automated Unit Tests passed (`tests/test_recommender.py`).

---

## Slide 7: Live Demonstration Walkthrough (5-7 Minutes)
1. **Scenario 1 (Normal Search)**: Select Cairo, High Budget, History + Museum tags $\rightarrow$ AI recommends NMEC, Museum of Islamic Art, and Coptic Museum.
2. **Scenario 2 (Wheelchair & Budget Constraint)**: Select Low Budget, Wheelchair = Yes $\rightarrow$ Filters output accessible low-cost sites.
3. **Scenario 3 (No Tags / Cold Start)**: Select no tags $\rightarrow$ System falls back to Popularity Baseline.

---

## Slide 8: Limitations, Ethics & Future Work
- **Limitations**: Prototype limited to Cairo & Giza (academic prototype scope).
- **Ethics**: Transparent explanations ("Reason: matches selected interests & active filters"), no hidden promotional bias.
- **Future Work**: Adding Google Maps distance routing and multi-day itinerary planning.
