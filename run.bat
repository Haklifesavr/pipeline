@echo off
python main.py
python -m unittest discover -s . -p "*new_tests.py"