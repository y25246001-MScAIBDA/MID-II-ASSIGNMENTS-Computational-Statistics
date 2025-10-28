"""
------------------------------------------------------------
Program Title : Probability and Random Numbers
Author        : Deepak Sharma 
Description   : This program demonstrates probability concepts
                and generation of random numbers using Python.
------------------------------------------------------------
"""

import random

# ---------------------------
# Step 1: Simulate a dice roll
# ---------------------------
outcomes = [1, 2, 3, 4, 5, 6]
roll = random.choice(outcomes)

# Probability of rolling an even number
even_numbers = [2, 4, 6]
prob_even = len(even_numbers) / len(outcomes)

# ---------------------------
# Step 2: Generate random numbers
# ---------------------------
rand_int = random.randint(1, 100)
rand_float = random.random()  # Between 0 and 1
rand_sample = random.sample(range(1, 50), 5)

# ---------------------------
# Step 3: Display results
# ---------------------------
print("----- Results -----")
print("Dice rolled:", roll)
print("Probability of even number:", prob_even)
print("Random Integer (1–100):", rand_int)
print("Random Float (0–1):", rand_float)
print("Random Sample of 5 numbers (1–50):", rand_sample)

"""
Explanation:
1. random.choice() selects one element randomly.
2. Probability of event = favorable outcomes / total outcomes.
3. random.randint() generates a random integer.
4. random.random() generates a random float in [0,1).
5. random.sample() gives unique random numbers.
"""
