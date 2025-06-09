# Statistical Language Models for Turkish

**StatLM-Turk** provides robust implementations of syllable-based and character-based N-gram language models for Turkish text, complete with smoothing, perplexity evaluation, and sentence generation utilities.

---

## 🚀 Features

* **Data Preparation**: Clean, normalize, and syllabify Turkish text.
* **N-Gram Modeling**: Build unigram, bigram, and trigram models at both character and syllable levels.
* **Smoothing**: Apply Good–Turing smoothing to handle unseen N‑grams.
* **Perplexity Evaluation**: Compute and compare model perplexities on held-out data.
* **Sentence Generation**: Sample fluent Turkish sentences from any N‑gram model.

---

## 📦 Prerequisites

* Python 3.8+
* pip (Python package manager)

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/emretechno/Statistical-Language-Model.git
   cd Statistical-Language-Model
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### 1. Data Preparation

Prepare your raw Turkish corpus (UTF‑8 encoded). By default, the script expects data in `DataPreparation/`. Normalize and syllabify:

```bash
python DataPreparation/prepare_data.py \
  --input path/to/raw_corpus.txt \
  --output DataPreparation/processed_corpus.txt
```

### 2. Train N‑Gram Models

Generate character and syllable N‑gram counts with smoothing:

```bash
python NGramCalculation/train_models.py \
  --input DataPreparation/processed_corpus.txt \
  --output models/ \
  --max_n 3 \
  --smoothing good_turing
```

### 3. Evaluate Perplexity

Compute perplexity on a test set:

```bash
python NGramCalculation/evaluate_perplexity.py \
  --models models/ \
  --test_data path/to/test_corpus.txt
```

### 4. Generate Random Sentences

Sample sentences from any trained model:

```bash
python RandomSentence/generate.py \
  --model models/char_trigram.pkl \
  --num_sentences 5
```

---

## 📊 Results

* Detailed perplexity comparisons across models are saved to `results/perplexity_results.csv`.
* Randomly generated sentences for each N‑gram level appear in `results/generated_sentences.txt`.
* See `REPORT/analysis.pdf` for in-depth performance analysis and visualizations.

---

## 📁 Project Structure

```
Statistical-Language-Model/
├── DataPreparation/        # Text cleaning & syllable segmentation scripts
├── NGramCalculation/       # N‑gram count, smoothing & evaluation modules
├── RandomSentence/         # Sentence sampling utilities
├── REPORT/                 # Analysis reports & figures
├── models/                 # Trained model artifacts (output)
├── results/                # Perplexity & generated sentences outputs
├── run.py                  # Quick-run entry point
├── requirements.txt        # Python dependencies
└── LICENSE                 # Project license
```

---

## 🤝 Contributing

Contributions are welcome! Please fork, create a feature branch, and submit a pull request.
Ensure any new code includes appropriate tests and documentation.

---

