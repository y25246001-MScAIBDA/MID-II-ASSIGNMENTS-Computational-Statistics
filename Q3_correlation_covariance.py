"""
------------------------------------------------------------
Program Title : Correlation and Covariance
Author        : Deepak Sharma 
Description   : This program computes covariance and correlation
                between two datasets using NumPy and statistics.
------------------------------------------------------------
"""

import numpy as np
import statistics as stats

# ---------------------------
# Step 1: Create sample datasets
# ---------------------------
x = [10, 20, 30, 40, 50]
y = [5, 10, 15, 20, 25]

# ---------------------------
# Step 2: Calculate Covariance
# ---------------------------
cov_matrix = np.cov(x, y, bias=False)
cov_xy = cov_matrix[0, 1]

# ---------------------------
# Step 3: Calculate Correlation
# ---------------------------
corr_val = stats.correlation(x, y)

# ---------------------------
# Step 4: Display Results
# ---------------------------
print("----- Results -----")
print("X:", x)
print("Y:", y)
print("Covariance:", cov_xy)
print("Correlation:", corr_val)

"""
Explanation:
1. Covariance shows how two variables vary together.
2. Correlation measures the strength and direction of the linear relationship (from -1 to +1).
3. np.cov() creates a covariance matrix.
4. stats.correlation() gives Pearson correlation coefficient.
"""
