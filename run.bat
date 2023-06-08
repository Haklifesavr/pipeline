@echo off
python -m venv .venv
cd .venv/scripts
.\activate
cd ../..
pip install -r requirements.txt
python main.py
python -m unittest discover -s . -p "*new_tests.py"