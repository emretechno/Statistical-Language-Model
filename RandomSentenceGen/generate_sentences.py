import random
import re
from collections import Counter

def is_valid_ngram(ngram):
    """ Check if the n-gram contains only valid characters: alphabetic, punctuation, and numbers. """
    return all(re.match(r'^[a-z0-9.,!?;:\'\"()\-]+$', word) for word in ngram)

def generate_sentence(ngram_counts, n, top_n=5, max_sentence_length=40):
    sentence = []
    # Count the n-grams
    ngram_counter = Counter(ngram_counts)
    # Filter valid n-grams for the initial selection
    valid_top_ngrams = [ngram for ngram, _ in ngram_counter.most_common() if is_valid_ngram(ngram)]
    if not valid_top_ngrams:
        return "No valid n-grams to generate a sentence."

    # Choose an initial n-gram from the top 5 valid options
    current_ngram = random.choice(valid_top_ngrams[:top_n])
    sentence.extend(current_ngram) # Add the initial n-gram to the sentence

    while len(sentence) < max_sentence_length:
        # Define context for the next n-gram
        context = tuple(sentence[-(n-1):]) if n > 1 else ()
        possible_ngrams = [ngram for ngram, _ in ngram_counter.items() if ngram[:n-1] == context]

        # Filter valid n-grams and take the top 5
        valid_possible_ngrams = [ngram for ngram in possible_ngrams if is_valid_ngram(ngram)]

        top_valid_ngrams = valid_possible_ngrams[:top_n]

        if not top_valid_ngrams:
            break  # No more valid n-grams

        # Select the next n-gram randomly from the top 5 valid options
        next_ngram = random.choice(top_valid_ngrams)
        sentence.append(next_ngram[-1])  # Add only the new word to the sentence

    return ' '.join(sentence)
