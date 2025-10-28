"""
------------------------------------------------------------
Program Title : Mean, Median, Mode, and Weighted Mean
Author        : Deepak Sharma 
Description   : This program calculates the mean, median, mode,
                and weighted mean of a given dataset using Python.
------------------------------------------------------------
"""

# Import necessary libraries
import statistics as stats     # For mean, median, and mode calculations
import numpy as np             # For weighted mean calculation
from collections import Counter  # For handling multiple modes

# ---------------------------
# Step 1: Create a sample dataset
# ---------------------------
data = [12, 7, 9, 12, 15, 9, 10, 12]

# ---------------------------
# Step 2: Calculate Mean
# ---------------------------
mean_val = stats.mean(data)   # Average of all values

# ---------------------------
# Step 3: Calculate Median
# ---------------------------
median_val = stats.median(data)  # Middle value when sorted

# ---------------------------
# Step 4: Calculate Mode
# ---------------------------
try:
    # Some Python versions return only one mode
    mode_val = stats.mode(data)
except:
    # Handle multiple modes manually
    freq = Counter(data)
    max_freq = max(freq.values())
    mode_val = [k for k, v in freq.items() if v == max_freq]

# ---------------------------
# Step 5: Calculate Weighted Mean
# ---------------------------
weights = [1, 1, 2, 1, 1, 1, 1, 1]   # Example weights
weighted_mean = np.average(data, weights=weights)

# ---------------------------
# Step 6: Display Results
# ---------------------------
print("----- Results -----")
print("Data: ", data)
print("Mean: ", mean_val)
print("Median: ", median_val)
print("Mode: ", mode_val)
print("Weighted Mean: ", weighted_mean)

"""
---------------------------
Explanation of Each Step:
---------------------------
1. 'import statistics' and 'import numpy' - provide built-in functions for statistical operations.
2. 'data' - represents the dataset of numeric values.
3. 'stats.mean(data)' - computes the arithmetic average.
4. 'stats.median(data)' - finds the middle value.
5. 'stats.mode(data)' - finds the most frequent number; manual logic handles multiple modes.
6. 'np.average(data, weights)' - calculates weighted mean.
7. 'print()' - displays all results clearly.
"""
