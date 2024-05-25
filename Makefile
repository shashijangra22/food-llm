# Makefile for FastAPI project

# Create and activate a virtual environment
env:
	python3 -m venv venv

# Install dependencies
install:
	. venv/bin/activate && pip install -r requirements.txt

# Run the FastAPI application
run-server:
	. venv/bin/activate && uvicorn main:app --reload --loop asyncio

# Run the streamlit application
run-app:
	. venv/bin/activate && streamlit run app.py