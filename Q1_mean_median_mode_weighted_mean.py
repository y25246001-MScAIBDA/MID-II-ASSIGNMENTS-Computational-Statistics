# Programming Task Q1
This Python program calculates the mean, median, mode, and weighted mean of a dataset.
# Q1: mean, median, mode, weighted mean

import statistics as stats
import numpy as np

# 1) sample dataset
data = [12, 7, 9, 12, 15, 9, 10, 12]

# 2) mean
mean_val = stats.mean(data)

# 3) median
median_val = stats.median(data)

# 4) mode (may return one value; if multiple modes exist, we handle manually)
try:
    mode_val = stats.mode(data)
except:
    # handle multimodal manually
    from collections import Counter
    freq = Counter(data)
    max_freq = max(freq.values())
    mode_val = [k for k, v in freq.items() if v == max_freq]

# 5) weighted mean
weights = [1, 1, 2, 1, 1, 1, 1, 1]  # same length as data
weighted_mean = np.average(data, weights=weights)

# 6) print results
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
print("Weighted Mean:", weighted_mean)
