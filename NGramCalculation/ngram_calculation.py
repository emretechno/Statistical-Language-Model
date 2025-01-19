
from nltk.util import ngrams
from collections import defaultdict
from collections import Counter


def get_ngram_counts(data, n):
    
    ngram_counts = defaultdict(float)  #Will be storaged with defaultdict to avoid KeyError
    for line in data:  # Iterate over each line in the data
        tokens = line.split()
        ngrams_in_line = ngrams(tokens, n) #ngrams function from nltk.util to generate n-grams for the current line.
        for ngram in ngrams_in_line:
            ngram_counts[ngram] += 1 # Count the n-grams in the data and store them in a dictionary 
                                     # with the n-gram as the key and the count as the value
    return ngram_counts


def calculate_n_grams(data , n ):
       return get_ngram_counts(data, n)


def get_frequency_of_ngrams(ngram_counts):
    frequency_of_ngrams = defaultdict(float)
    count_frequencies = Counter(ngram_counts)
    total_ngrams = sum(count_frequencies.values()) #Total number of n-grams count_frequencies.items()   
    #returns a list of tuples where each tuple contains an n-gram and its count

    for ngram, count in count_frequencies.items(): # count_frequencies = {('I', 'am'): 3, ('am', 'awesome'): 2}
        frequency_of_ngrams[ngram] = count / total_ngrams #Total count of n-grams divided by the number of n-grams to get the frequency of each n-gram
    return frequency_of_ngrams # frequency_of_ngrams = {('I', 'am'): 0.6, ('am', 'awesome'): 0.4} 


