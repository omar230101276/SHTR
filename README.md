# Smart Heritage Tourism Recommender (SHTR)

An AI-powered academic prototype recommender system for tourism and heritage attractions in Cairo and Giza. Built for the **CET 251 Artificial Intelligence** course (Academic Year 2026).

---

## 🌟 Key Features

- **Hard Constraints Filtering (CSP Concept)**: Filters places strictly by Location, Budget, Available Time, Opening Period, and Wheelchair Accessibility.
- **AI Recommendation Engine**: Uses **TF-IDF Vectorization & Cosine Similarity** to match visitor interests with attraction tags.
- **Popularity Baseline Model**: Provides a rule-based baseline ranking for comparative evaluation.
- **Quantitative Evaluation**: Displays live **Filter Match Rate** metrics on every search query.
- **Interactive Web Interface**: Built with **Streamlit** for quick and intuitive demonstration.

---

## 📁 Repository Structure

```text
SHTR/
├── README.md                          # Main project overview and instructions
├── requirements.txt                   # Python package dependencies
├── app.py                             # Main Streamlit web application
├── run.py                             # Python launcher script
├── run.bat                            # Windows 1-click launcher script
├── data/
│   ├── raw/
│   │   └── egypt_attractions.csv      # 40 curated attractions dataset
│   └── processed/
├── src/
│   ├── data_processing.py             # Data loading & hard constraint filters
│   ├── model.py                       # TF-IDF Cosine Similarity & Baseline models
│   ├── evaluation.py                  # Filter Match Rate metric calculation
│   └── train.py                       # Model training & artifact export script
├── models/
│   ├── tfidf_vectorizer.joblib        # Saved TF-IDF vectorizer artifact
│   └── tfidf_matrix.joblib            # Saved feature matrix artifact
├── notebooks/
│   └── 01_recommender_pipeline.ipynb  # 7-step lab pipeline Jupyter notebook
├── tests/
│   ├── test_recommender.py            # Automated unittest test suite (9 tests)
│   └── test_report.md                 # Appendix C test cases & results
├── docs/
│   ├── Project_Proposal.pdf           # Appendix A project proposal
│   ├── Smart_Heritage_Tourism_Final_Report.pdf # Appendix B final technical report
│   ├── data_dictionary.pdf            # PDF Data Dictionary
│   ├── data_dictionary.md             # Markdown Data Dictionary
│   ├── presentation_slides.md         # Appendix E 6-8 slide demo presentation
│   └── contribution_statement.md      # Appendix E academic integrity declaration
└── deployment/
    └── setup_instructions.md          # Appendix D setup & reproducibility guide
```

---

## 🚀 Quick Start Guide

### 1. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. (Optional) Re-train the AI Model
```bash
python src/train.py
```

### 3. Run the Web Application
Choose any of the following methods:
- **Windows Double-Click**: Double-click `run.bat`
- **Python Launcher**: `python run.py`
- **Streamlit CLI**: `python -m streamlit run app.py`

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🧪 Running Automated Tests

Run the full suite of 9 unit tests verifying all 8 required test cases:
```bash
python -m unittest discover -s tests
```

---

## 📊 Dataset Overview

The project uses a curated dataset of **40 heritage sites** across Cairo and Giza (`data/raw/egypt_attractions.csv`). Attributes include:
- `id`, `name`, `location` (Cairo / Giza)
- `category` (Pharaonic, Islamic, Coptic, Modern, Nature, Culture, Jewish)
- `duration_hours` (1 to 4 hours)
- `cost_level` (Low, Medium, High)
- `opening_period` (Morning, Evening, Full Day)
- `wheelchair_accessible` (Yes, No)
- `indoor_outdoor` (Indoor, Outdoor, Both)
- `tags` (Textual descriptive keywords for TF-IDF matching)

---

## 📐 AI Architecture & Metrics

1. **Filtering Layer**: Hard constraints eliminate options that exceed available user hours or budget bounds.
2. **Scoring Layer**: 
   $$\text{Score} = \text{CosineSimilarity}(\vec{v}_{\text{user}}, \vec{v}_{\text{attraction}})$$
3. **Metric**:
   $$\text{Filter Match Rate} = \left( \frac{\text{Matching Recommendations}}{\text{Total Recommendations}} \right) \times 100\%$$

---

## 📄 License & Academic Declaration

Prepared for **CET 251 Artificial Intelligence**, Supervised by **Dr. Mohamed Aly Saleh**.