import multiprocessing  # For parallel processing
import math  # For mathematical operations
import sys  # For system-level settings
import time  # For measuring execution time

# Set the maximum number of digits for integer strings (Python 3.11+)
# This is useful for handling large numbers, though not necessary in this case
sys.set_int_max_str_digits(100000)

# Function to compute the factorial of a given number
def compute_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)  # Calculate the factorial using math.factorial
    print(f'Factorial of {number} is {result}')
    return result

# Main block of code to ensure multiprocessing works as intended
if __name__ == "__main__":
    # List of numbers for which factorials will be computed
    numbers = [500, 6000, 700, 8000]

    # Record the start time to measure performance
    start_time = time.time()

    # Create a pool of worker processes for parallel computation
    with multiprocessing.Pool() as pool:
        # Distribute the computation of factorials across processes
        results = pool.map(compute_factorial, numbers)

    # Record the end time after computation
    end_time = time.time()

    # Print the results of the factorial calculations
    print(f'Result: {results}')

    # Calculate and print the total time taken for computation
    print(f'Time taken: {end_time - start_time} seconds')
