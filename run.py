import os
import subprocess
import sys

def main():
    print("Starting Smart Heritage Tourism Recommender...")
    
    # Ensure current working directory is the project directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, "app.py")

    cmd = [sys.executable, "-m", "streamlit", "run", app_path]
    subprocess.run(cmd, cwd=script_dir)

if __name__ == "__main__":
    main()
