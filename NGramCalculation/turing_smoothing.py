from collections import defaultdict, Counter



def good_turing_smoothing(ngram_counts, total_ngrams):

    frequency_of_n_grams = Counter(ngram_counts.values())  # Counts the frequency of each n-gram count in the data
    smoothed_ngram_counts = defaultdict(float) # I will  stored the smoothed probabilities of n-grams later.

    for ngram, count in ngram_counts.items(): # Iterate over the n-grams and their counts
        if count + 1 in frequency_of_n_grams: # If there are N-grams with count + 1

            # Adjust the count using Good-Turing formula
            adjusted_count = (count + 1) * frequency_of_n_grams.get(count + 1, 0) / frequency_of_n_grams.get(count, 1)
            # frequency_of_n_grams.get(count + 1, 0) returns the frequency of N-grams with count + 1
        else:
            adjusted_count = count  # If there's no N-gram with count + 1, leave it unchanged

        # Normalize by the total number of N-grams
        smoothed_ngram_counts[ngram] = adjusted_count / total_ngrams


    N1 = frequency_of_n_grams.get(1, 0)# N1 is the number of N-grams that occur exactly once. ( 1 , 0 ) means if there is no N-gram that occurs exactly once, return 0.

    unseen_prob = N1 / total_ngrams if total_ngrams > 0 else 0  # Good-Turing estimate for unseen N-grams

    return smoothed_ngram_counts, unseen_prob

