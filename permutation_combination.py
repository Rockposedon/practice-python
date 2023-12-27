'''
        calculating permutation and combination
'''
from sample_one_fact import *

# Get input values for n and r
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Calculating permutation:
if n > r:
    # Call the facto function from the imported module to calculate factorial
    n_fact = facto(n)
    n_minus_r_fact = facto(n - r)
    result_permutation = n_fact / n_minus_r_fact
    print("Permutation is:", result_permutation)
elif n == r:
    r_fact = facto(n)
    print("Permutation is:", r_fact)
else:
    print("n must be greater than or equal to r, please enter valid values.")

# Calculating combination:
if n > r:
    r_fact = facto(r)
    n_minus_r_fact = facto(n - r)
    result_combination = n_fact / (r_fact * n_minus_r_fact)
    print("Combination is:", result_combination)
elif n == r:
    print("Combination is:", 1)
else:
    print("n must be greater than or equal to r, please enter valid values.")
