# Statistical Language Models for Turkish

This project implements and analyzes **syllable-based** and **character-based N-gram language models** for Turkish text. The models calculate N-gram probabilities, evaluate perplexity, and generate random sentences to compare performance.

## Features
- **Data Preparation**: Processes Turkish text using syllable segmentation and character normalization.
- **N-Gram Calculation**: Builds 1-Gram, 2-Gram, and 3-Gram models with **Good-Turing smoothing**.
- **Random Sentence Generation**: Generates sentences using N-gram probabilities.
- **Performance Evaluation**: Calculates perplexity and compares models.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emretechno/Statistical-Language-Model
   cd 210104004017_YUSUF_PROJECT

## Install the required Python packages:

pip install -r requirements.txt

## Run the project

python run.py

## Results
- Perplexity values for syllable-based and character-based models.
- Random sentences generated for different N-gram levels.
- Analysis and conclusions on model performance.


## Project Structure

210104004017_YUSUF_PROJECT/
├── DataPreparation/        # Scripts for data processing and normalization
├── NGramCalculation/       # Scripts for N-gram calculation and smoothing
├── RandomSentence/         # Script for random sentence generation
├── REPORT/                 # Report files and documentation
├── run.py                  # Main script to execute the project
├── makefile                # Build and setup commands
├── requirements.txt        # Python dependencies
└── readme.md               # Project documentation

## NOTE 
- The data is not included due to its gigantic size. Can be provided if it is needed.
- All Turkish characters are normalized (e.g., ş -> s, ğ -> g).
- N-gram probabilities are calculated with logarithms to avoid underflow issues.
- Generated sentences are included in the report for analysis.
