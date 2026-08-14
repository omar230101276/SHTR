# Deployment & Reproducibility Guide (Appendix D)

This document provides step-by-step instructions to set up, train, test, and deploy the **Smart Heritage Tourism Recommender (SHTR)** prototype on any clean environment.

---

## 1. System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python Version**: Python 3.8 to 3.12
- **Memory**: Minimum 2 GB RAM
- **Disk Space**: 100 MB free space
- **Network**: Internet connection required ONLY for initial package installation. The application runs **100% offline** once installed.

---

## 2. Environment Setup

### Step 1: Open Terminal in Project Directory
Navigate to the root directory of `SHTR`:
```bash
cd path/to/SHTR
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv .venv
```
Activate the virtual environment:
- **Windows (CMD/PowerShell)**:
  ```powershell
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 3. Model Training & Offline Artifact Export

To train the TF-IDF vectorizer model and generate model artifacts:
```bash
python src/train.py
```
This generates the following files in the `models/` directory:
- `models/tfidf_vectorizer.joblib`
- `models/tfidf_matrix.joblib`

---

## 4. Launching the Prototype

### Option A: 1-Click Windows Launcher
Double-click `run.bat` in the project root directory.

### Option B: Python Launcher Script
```bash
python run.py
```

### Option C: Direct Streamlit CLI
```bash
python -m streamlit run app.py
```

Once started, open your browser at **`http://localhost:8501`**.

---

## 5. Verification & Automated Tests

To run the full suite of automated unit tests:
```bash
python -m unittest discover -s tests
```
Expected output:
```text
Ran 9 tests in 0.100s
OK
```

---

## 6. Reproducibility Checklist (Appendix D Verification)

- [x] **No Paid APIs**: Code uses open-source `scikit-learn` and local CSV datasets.
- [x] **Relative Paths**: All file paths are relative to the project root.
- [x] **Offline Execution**: Runs without external API keys or cloud dependencies.
- [x] **Clean Startup**: Launches with a single command (`python run.py` or `run.bat`).
