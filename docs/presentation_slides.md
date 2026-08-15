# Smart Heritage Tourism Recommender (SHTR)
## Official Final Demo Presentation Slide Deck Outline

**Course**: CET 251 – Artificial Intelligence (Academic Year 2026)  
**Project ID**: D4  
**Instructor**: Dr. Mohamed Aly Saleh  
**Team Members**: Reyad Hamdy (240103466), Omar Abdelghany (230101276), Kirellos Samir (230102253)

---

### Slide 1: Title Slide & Project Metadata
- **Title**: Smart Heritage Tourism Recommender (SHTR)
- **Subtitle**: AI-Powered Multi-Constraint Recommendation System for Cairo & Giza
- **Academic Context**: CET 251 Artificial Intelligence, Project D4, Academic Year 2026
- **Supervision**: Supervised by Dr. Mohamed Aly Saleh
- **Team**: Reyad Hamdy (240103466), Omar Abdelghany (230101276), Kirellos Samir (230102253)

---

### Slide 2: Problem Definition & Motivation
- **Tourism Information Overload**: Cairo & Giza feature hundreds of heritage landmarks across 5,000+ years of history.
- **Conflicting Constraints**: Travelers operate under hard constraints: budget limits, available visit hours, geographical location, operating windows, and wheelchair mobility needs.
- **Standard Search Engine Limitation**: Traditional search engines fail to combine hard boolean constraint satisfaction with soft vector interest similarity.
- **The SHTR Solution**: Dual-layer architecture providing 100% hard constraint compliance + TF-IDF Cosine Similarity recommendation + category diversity filtering.

---

### Slide 3: Curated Cairo & Giza Dataset Architecture
- **Dataset Size**: 40 curated heritage landmarks across Cairo and Giza.
- **7 Heritage Categories**: Pharaonic, Islamic, Coptic, Modern, Nature, Culture, and Jewish.
- **10 Core Attributes**: `id`, `name`, `location`, `category`, `duration_hours`, `cost_level`, `opening_period`, `wheelchair_accessible`, `indoor_outdoor`, `tags`.
- **Keyword Tags**: Space-separated interest tags enabling sparse vector space modeling.

---

### Slide 4: AI Formulation & Dual Engine Architecture
- **Layer 1 (Constraint Satisfaction Problem Engine)**: Evaluates strict boolean masks for location, budget upper bound, duration hours, visit period, and wheelchair accessibility *prior* to similarity scoring.
- **Layer 2 (Content-Based AI Engine)**: Vectorizes user interest multiselect tags and item keywords using TF-IDF and computes pairwise Cosine Similarity.
- **Category Diversity Enforcer**: Deduplicates top recommendations to prevent returning multiple items from the same category.
- **Popularity Baseline Fallback**: Cold-start fallback model for queries without specified interest tags.

---

### Slide 5: Mathematical Formulation
- **TF-IDF Term Weighting**:
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \log\left(\frac{N}{|\{d \in D : t \in d\}|}\right)$$
- **Cosine Similarity Vector Angle**:
  $$\text{Cosine Similarity}(\vec{v}_{\text{user}}, \vec{v}_{\text{item}}) = \frac{\vec{v}_{\text{user}} \cdot \vec{v}_{\text{item}}}{\|\vec{v}_{\text{user}}\| \|\vec{v}_{\text{item}}\|}$$

---

### Slide 6: System Operational Workflow (4-Phase Architecture)
- **Phase 1 (Data & Input)**: Load CSV dataset (40 records) & capture user UI inputs.
- **Phase 2 (Constraint Engine)**: Execute `apply_hard_filters()`, check empty results, route cold-start queries.
- **Phase 3 (TF-IDF & Similarity Engine)**: Load `models/tfidf_vectorizer.joblib`, compute similarity matrix $S \in [0, 1]$, sort scores descending.
- **Phase 4 (Output & Evaluation)**: Deduplicate categories (Top 3), render results & live 100% Filter Match Rate metric.

---

### Slide 7: Software Engineering & Modular Codebase
- **`src/data_processing.py`**: Data loading and hard constraint CSP boolean filters.
- **`src/model.py`**: TF-IDF Cosine Similarity engine & popularity baseline generator.
- **`src/evaluation.py`**: Live Filter Match Rate (FMR) calculation engine.
- **`src/train.py`**: Offline model training script exporting `models/tfidf_vectorizer.joblib`.
- **`app.py` & `run.py` / `run.bat`**: Interactive Streamlit dashboard & 1-click launchers.
- **`notebooks/01_recommender_pipeline.ipynb`**: 7-step lab pipeline notebook.

---

### Slide 8: Evaluation & Experimental Results
- **Quantitative Evaluation Metric**: Filter Match Rate (FMR):
  $$\text{Filter Match Rate} = \left( \frac{\text{Recommended items satisfying active hard filters}}{\text{Total recommendations returned}} \right) \times 100\%$$
- **Target**: 100.0% | **Observed Performance**: **100.0% FMR** across all queries.
- **Observed Persona Results**:
  - History & Museum: Abdeen Palace Museum (40.1% similarity) | FMR: 100.0%
  - Culture & Heritage: Sultan Hassan Mosque (25.4% similarity) | FMR: 100.0%
  - Giza Exploration: Memphis Open-Air Museum (27.0% similarity) | FMR: 100.0%
  - Nature & Relaxation: Al-Azhar Park (50.2% similarity) | FMR: 100.0%

---

### Slide 9: Quality Assurance & Automated Test Suite
- **Framework**: Python `unittest` (`tests/test_recommender.py`).
- **9 Automated Unit Tests** verifying 8 Core Test Scenarios:
  - TC-01 Normal Recommendation Pipeline & Top 3 sorting: **PASS**
  - TC-02 Low Budget & Short Duration constraint filtering: **PASS**
  - TC-03 Giza Location filtering: **PASS**
  - TC-04 Wheelchair Accessibility enforcement: **PASS**
  - TC-05 Morning Visit Period filtering: **PASS**
  - TC-06 No Interests Selected (Popularity baseline fallback): **PASS**
  - TC-07 Contradictory Filters Edge Case (Graceful warning banner): **PASS**
  - TC-08 Dynamic Interest Tag scoring: **PASS**
  - Metric Verification Test (Automated 100% FMR check): **PASS**

---

### Slide 10: Conclusion & Future Enhancement Roadmap
- **Key Accomplishments**: Fulfilled all D4 requirements, 100% Filter Match Rate compliance, modular code structure, persistent AI artifacts, automated unittest suite.
- **Future Roadmap**:
  - Live GPS & Route Optimization for multi-stop tours.
  - Dynamic API integration for Ministry ticket prices & live operating hours.
  - Search algorithm itinerary planning (A* / Genetic Algorithms).
  - Collaborative filtering based on anonymized tourist ratings.
