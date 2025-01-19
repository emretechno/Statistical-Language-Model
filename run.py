
#~~~~~~~~~~~~~~~~~~~~~~~               IMPORTING                               ~~~~~~~~~~~~~~~~~~~~~~~§
import sys,os,re,random
#Need to add the parent directory to the sys.path in order to import the modules on other folders.
#import other folders at the same place with this current file

def append_path(folder_name):
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), folder_name))
    sys.path.append(directory)

append_path('RandomSentenceGen')
append_path('DataPreparation')
append_path('NGramCalculation')

from DataPreparation.normalize_text import normalize_the_file
from DataPreparation.process_char_syllable_model import process_data_syllable_model, process_data_char_based
from NGramCalculation.ngram_calculation import calculate_n_grams , get_frequency_of_ngrams
from NGramCalculation.turing_smoothing import good_turing_smoothing
from NGramCalculation.calculate_perplexity import  calculate_perplexity
from RandomSentenceGen.generate_sentences import generate_sentence
from sklearn.model_selection import train_test_split
from collections import Counter

file_path = 'DataPreparation/wiki_00'  # No leading space here

#~~~~~~~~~~~~~~~~~~~~~~~               READING FILE AND NORMALIZING                              ~~~~~~~~~~~~~~~~~~~~~~~§
print(f"*_* Normalizing the file {file_path}")

#normalize_the_file(file_path)

print(f"*_* Reading the file now....")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines
lines = read_file(file_path)


print(f"    File was read successfully.\n");

#~~~~~~~~~~~~~~~~~~~~~~~              TRAINING DATA                          ~~~~~~~~~~~~~~~~~~~~~~~§

# Step 2: Split the dataset (95% train, 5% test)
print("*_* Splitting the dataset into train and test data....")

train_data, test_data = train_test_split(lines, test_size=0.05, random_state=42)



'''

When the Random_state is not defined in the code for every run train data will change
and accuracy might change for every run. When the Random_state = " constant integer" is defined 
then train data will be constant For every run so that it will make easy to debug.

'''

print(f"    The dataset splitted succesfully.\n")
#~~~~~~~~~~~~~~~~~~~~~~~             CHAR_BASED AND SYLLABLE_BASED TRAINING AND TEST DATA  ~~~~~~~~~~~~~~~~~~~~~~~§

# Step 3: Process the train and test data using process_data

print("*_* Processing the train and test data based on syllable-model and char-model....")

syllable_processed_train_data = process_data_syllable_model(train_data)
syllable_processed_test_data = process_data_syllable_model(test_data)

char_processed_train_data = process_data_char_based(train_data)
char_processed_test_data = process_data_char_based(test_data)

print(f"    Data processed based on the models  successfully.\n")

# Step 4: Output some results
'''
print(f"Number of lines in the training data: {len(syllable_processed_train_data)}")
print(f"Number of lines in the testing data: {len(syllable_processed_test_data)}")

print("Sample from training data:")
for line in syllable_processed_train_data[:5]:
    print(line)

print("\nSample from testing data:")
for line in syllable_processed_test_data[:5]:
    print(line)

print(f"The sample from char processed training data in charbased: {char_processed_train_data[:5]}")
print(f"The sample from char processed test data char based: {char_processed_test_data[:5]}")

'''

# Get the counts of 2-grams in the training data



#~~~~~~~~~~~~~~~~~~~~~~~             N-GRAM CALCULATION AND SMOOTHING  ~~~~~~~~~~~~~~~~~~~~~~~§
print("*_* Calculating the 1,2 and 3 grams for both syllable and char based models.... for train and test data.")

syllable_1gram_train_counts = calculate_n_grams(syllable_processed_train_data, 1) #return a dictionary
syllable_1gram_test_counts = calculate_n_grams(syllable_processed_test_data, 1) 
char_1gram_train_counts = calculate_n_grams(char_processed_train_data, 1) 
char_1gram_test_counts = calculate_n_grams(char_processed_test_data, 1) 

syllable_2gram_train_counts = calculate_n_grams(syllable_processed_train_data, 2)
syllable_2gram_test_counts = calculate_n_grams(syllable_processed_test_data,2)
char_2gram_train_counts = calculate_n_grams(char_processed_train_data, 2)
char_2gram_test_counts = calculate_n_grams(char_processed_test_data, 2) 

syllable_3gram_train_counts = calculate_n_grams(syllable_processed_train_data, 3)
syllable_3gram_test_counts = calculate_n_grams(syllable_processed_test_data,3) 
char_3gram_train_counts = calculate_n_grams(char_processed_train_data, 3)
char_3gram_test_counts = calculate_n_grams(char_processed_test_data, 3) 

#~~~~~~~~~~~~~~~~~~~~~~~            CALCULATING THE SUMS OF N_GRAM COUNTS         ~~~~~~~~~~~~~~~~~~~~~~~§

total_syllable_1gram_train_counts = sum(syllable_1gram_train_counts.values())
total_char_1gram_train_counts = sum(char_1gram_train_counts.values())

total_syllable_2gram_train_counts = sum(syllable_2gram_train_counts.values())
total_char_2gram_train_counts = sum(char_2gram_train_counts.values()) 

total_syllable_3gram_train_counts = sum(syllable_3gram_train_counts.values())
total_char_3gram_train_counts = sum(char_3gram_train_counts.values())

#~~~~~~~~~~~~~~~~~~~~~~~           CALCULATE THE FREQUENCIES         ~~~~~~~~~~~~~~~~~~~~~~~§

syllable_1gram_freq = get_frequency_of_ngrams(syllable_1gram_train_counts)
char_1gram_freq = get_frequency_of_ngrams(char_1gram_train_counts)

syllable_2gram_freq = get_frequency_of_ngrams(syllable_2gram_train_counts)
char_2gram_freq = get_frequency_of_ngrams(char_2gram_train_counts)

syllable_3gram_freq = get_frequency_of_ngrams(syllable_3gram_train_counts)
char_3gram_freq = get_frequency_of_ngrams(char_3gram_train_counts)

'''
print("    The n-grams are calculated successfully.\n")

def print_ngrams(ngram_counts):

    ngram_counter = Counter(ngram_counts)

    # Print the top 10 n-grams
    for ngram, count in ngram_counter.most_common(10):

        # If the n-gram is a 1-gram, print it as a tuple
        if len(ngram) == 1:
            print(f"('{ngram[0]}')", count)
        else:
            print(ngram, count)

# Print the n-grams if the user wants to see them

print("The frequency of n-grams for char 1-gram:")
print_ngrams(char_1gram_freq)

print("The frequency of n-grams for char 2-gram:")
print_ngrams(char_2gram_freq)

print("The frequency of n-grams for char 3-gram:")
print_ngrams(char_3gram_freq)

print("The frequency of n-grams for syllable 1-gram:")
print_ngrams(syllable_1gram_freq)

print("The frequency of n-grams for syllable 2-gram:")
print_ngrams(syllable_2gram_freq)

print("The frequency of n-grams for syllable 3-gram:")
print_ngrams(syllable_3gram_freq)

print(f"Results of the n-grams:")
    
print(f"Top 10 1-grams in syllable-based model:")
print_ngrams(syllable_1gram_train_counts)

print(f"Top 10 2-grams in syllable-based model:")
print_ngrams(syllable_2gram_train_counts)

print(f"Top 10 3-grams in syllable-based model:")
print_ngrams(syllable_3gram_train_counts)

print(f"Top 10 1-grams in character-based model:")
print_ngrams(char_1gram_train_counts)

print(f"Top 10 2-grams in character-based model:")
print_ngrams(char_1gram_train_counts)

print(f"Top 10 3-grams in character-based model:")
print_ngrams(char_3gram_train_counts)
'''

      #~~~~~~~~~~~~~~~~~~~~~~~           SMOOTHING THE N-GRAMS         ~~~~~~~~~~~~~~~~~~~~~~~§

char_1gram_smoothed , char_1gram_unseen = good_turing_smoothing(char_1gram_train_counts, total_char_1gram_train_counts)
char_2gram_smoothed , char_2gram_unseen = good_turing_smoothing(char_2gram_train_counts, total_char_2gram_train_counts)
char_3gram_smoothed , char_3gram_unseen = good_turing_smoothing(char_3gram_train_counts, total_char_3gram_train_counts)

syllable_1gram_smoothed , syllable_1gram_unseen = good_turing_smoothing(syllable_1gram_train_counts, total_syllable_1gram_train_counts)
syllable_2gram_smoothed , syllable_2gram_unseen = good_turing_smoothing(syllable_2gram_train_counts, total_syllable_2gram_train_counts)
syllable_3gram_smoothed , syllable_3gram_unseen = good_turing_smoothing(syllable_3gram_train_counts, total_syllable_3gram_train_counts)

'''
def print_smoothed_ngrams(ngram_counts):
    
        ngram_counter = Counter(ngram_counts)
    
        # Print the top 10 n-grams
        for ngram, count in ngram_counter.most_common(10):
    
            # If the n-gram is a 1-gram, print it as a tuple
            if len(ngram) == 1:
                print(f"('{ngram[0]}')", count)
            else:
                print(ngram, count)



print("The smoothed n-grams for char 1-gram:")
print_smoothed_ngrams(char_1gram_smoothed)

print("The smoothed n-grams for char 2-gram:")
print_smoothed_ngrams(char_2gram_smoothed)

print("The smoothed n-grams for char 3-gram:")
print_smoothed_ngrams(char_3gram_smoothed)

print("The smoothed n-grams for syllable 1-gram:")
print_smoothed_ngrams(syllable_1gram_smoothed)

print("The smoothed n-grams for syllable 2-gram:")
print_smoothed_ngrams(syllable_2gram_smoothed)

print("The smoothed n-grams for syllable 3-gram:")
print_smoothed_ngrams(syllable_3gram_smoothed)

#unseen probs
print(f"The unseen probability for char 1-gram: {char_1gram_unseen}")
print(f"The unseen probability for char 2-gram: {char_2gram_unseen}")
print(f"The unseen probability for char 3-gram: {char_3gram_unseen}")

print(f"The unseen probability for syllable 1-gram: {syllable_1gram_unseen}")
print(f"The unseen probability for syllable 2-gram: {syllable_2gram_unseen}")
print(f"The unseen probability for syllable 3-gram: {syllable_3gram_unseen}")
'''
# Calculate the perplexity of the test data using the smoothed n-grams

char_1gram_perplexity = calculate_perplexity(char_1gram_test_counts, char_1gram_smoothed, char_1gram_unseen)
char_2gram_perplexity = calculate_perplexity(char_2gram_test_counts, char_2gram_smoothed, char_2gram_unseen)
char_3gram_perplexity = calculate_perplexity(char_2gram_test_counts, char_3gram_smoothed, char_3gram_unseen)
syllable_1gram_perplexity = calculate_perplexity(syllable_1gram_test_counts, syllable_1gram_smoothed, syllable_1gram_unseen)
syllable_2gram_perplexity = calculate_perplexity(syllable_2gram_test_counts, syllable_2gram_smoothed,syllable_2gram_unseen)
syllable_3gram_perplexity = calculate_perplexity(syllable_3gram_test_counts, syllable_3gram_smoothed, syllable_3gram_unseen)

print(f"The perplexity of the test data for char 1-gram: {char_1gram_perplexity}")
print(f"The perplexity of the test data for char 2-gram: {char_2gram_perplexity}")
print(f"The perplexity of the test data for char 3-gram: {char_3gram_perplexity}")

print(f"The perplexity of the test data for syllable 1-gram: {syllable_1gram_perplexity}")
print(f"The perplexity of the test data for syllable 2-gram: {syllable_2gram_perplexity}")
print(f"The perplexity of the test data for syllable 3-gram: {syllable_3gram_perplexity}")


# Generating a sentence with the syllable 1-gram model
syllable_1gram_sentence = generate_sentence(syllable_1gram_smoothed, 1)
print(f"Generated sentence (Syllable 1-gram): {syllable_1gram_sentence}")

# Generating a sentence with the syllable 2-gram model
syllable_2gram_sentence = generate_sentence(syllable_2gram_smoothed, 2)
print(f"Generated sentence (Syllable 2-gram): {syllable_2gram_sentence}")

# Generating a sentence with the syllable 3-gram model
syllable_3gram_sentence = generate_sentence(syllable_3gram_smoothed, 3)
print(f"Generated sentence (Syllable 3-gram): {syllable_3gram_sentence}")

# Generating a sentence with the character 1-gram model
char_1gram_sentence = generate_sentence(char_1gram_smoothed, 1)
print(f"Generated sentence (Character 1-gram): {char_1gram_sentence}")

# Generating a sentence with the character 2-gram model
char_2gram_sentence = generate_sentence(char_2gram_smoothed, 2)
print(f"Generated sentence (Character 2-gram): {char_2gram_sentence}")

# Generating a sentence with the character 3-gram model
char_3gram_sentence = generate_sentence(char_3gram_smoothed, 3)
print(f"Generated sentence (Character 3-gram): {char_3gram_sentence}")
