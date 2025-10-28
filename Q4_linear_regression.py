"""
------------------------------------------------------------
Program Title : Simple Linear Regression
Author        : <Your Name>
Description   : This program performs linear regression on two
                datasets (X and Y) to find slope, intercept, and
                predicted values using NumPy.
------------------------------------------------------------
"""

import numpy as np

# ---------------------------
# Step 1: Input data
# ---------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# ---------------------------
# Step 2: Calculate slope (m) and intercept (c)
# ---------------------------
m, c = np.polyfit(x, y, 1)

# ---------------------------
# Step 3: Predict values
# ---------------------------
y_pred = m * x + c

# ---------------------------
# Step 4: Display results
# ---------------------------
print("----- Results -----")
print("X:", x)
print("Y:", y)
print("Slope (m):", m)
print("Intercept (c):", c)
print("Predicted Y values:", y_pred)

"""
Explanation:
1. np.polyfit(x, y, 1) fits a straight line (degree = 1).
2. m = slope, c = intercept.
3. y_pred = predicted Y values using the regression equation.
"""
