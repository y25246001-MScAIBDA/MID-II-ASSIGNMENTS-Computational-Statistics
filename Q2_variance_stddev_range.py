"""
------------------------------------------------------------
Program Title : Variance, Standard Deviation, and Range
Author        : Deepak Sharma 
Description   : This program calculates the variance, standard
                deviation, and range of a dataset using Python.
------------------------------------------------------------
"""

# Import libraries
import statistics as stats

# ---------------------------
# Step 1: Create dataset
# ---------------------------
data = [8, 12, 9, 15, 10, 6, 9, 14]

# ---------------------------
# Step 2: Calculate Variance
# ---------------------------
variance_val = stats.variance(data)

# ---------------------------
# Step 3: Calculate Standard Deviation
# ---------------------------
std_dev_val = stats.stdev(data)

# ---------------------------
# Step 4: Calculate Range
# ---------------------------
range_val = max(data) - min(data)

# ---------------------------
# Step 5: Display Results
# ---------------------------
print("----- Results -----")
print("Data:", data)
print("Variance:", variance_val)
print("Standard Deviation:", std_dev_val)
print("Range:", range_val)

"""
Explanation:
1. Variance measures how far data points deviate from the mean.
2. Standard deviation is the square root of variance.
3. Range is the difference between the largest and smallest value.
"""
