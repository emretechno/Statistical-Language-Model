


import math

def calculate_perplexity(ngrams_in_test_data, smoothed_probabilities, unseen_prob):

   
    log_prob_sum = 0  # Sum of log probabilities
    total_ngrams_counted = len(ngrams_in_test_data)  # Total length of n-grams in the test data
    
    if total_ngrams_counted == 0:
        return float('inf')  # Avoid division by zero if no n-grams in test data

    # Calculate log probabilities for each n-gram
    for ngram in ngrams_in_test_data:
        # Use smoothed probability if available, else use the unseen probability
        prob = smoothed_probabilities.get(ngram, unseen_prob)
        
        log_prob_sum += -math.log(prob)

    # Compute perplexity
    perplexity = math.exp(log_prob_sum / total_ngrams_counted)
    return perplexity
