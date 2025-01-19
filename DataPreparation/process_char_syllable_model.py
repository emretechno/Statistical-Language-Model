import re
from sklearn.model_selection import train_test_split
from segment_syllable import segment_syllables
from normalize_text import  normalize_turkish_to_english


def process_data_syllable_model(data):
    processed_lines = []
    for line in data:  # Iterate over each line in the data
        if line.strip() == "":  # Skip empty lines
            continue
        words = line.split()  # First split the line into words
        syllable_segmented_line = " ".join([syllable for word in words for syllable in segment_syllables(word)])  # Segment each word into syllables and treat them as separate words
        processed_lines.append(syllable_segmented_line)
    return processed_lines


# Function to process data for a character-based model
def process_data_char_based(data):
    processed_lines = []
    for line in data:  # Iterate over each line in the data
        if line.strip() == "":  # Skip empty lines
            continue
        # Treat each character as a token, join the characters with spaces
        char_segmented_line = " ".join(line)  # Add spaces between characters
        
        processed_lines.append(char_segmented_line)
    
    return processed_lines



