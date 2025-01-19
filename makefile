# Makefile to run the Python script and install dependencies

# Define the default target
all: install run

# Install dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run the Python script
run:
	python3 run.py
