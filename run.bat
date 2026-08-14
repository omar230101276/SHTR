@echo off
cd /d "%~dp0"
echo Starting Smart Heritage Tourism Recommender...
python -m streamlit run app.py
pause
