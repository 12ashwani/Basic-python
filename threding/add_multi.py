from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)  # Simulate a delay
    result = number ** 2
    print(f"Square of {number}: {result}")
    return result  # Return the result

if __name__ == "__main__":  # Corrected __name__ check
    numbers = [1, 3, 4, 5, 5]  # Input numbers
    
    # Use ProcessPoolExecutor to run tasks in parallel
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)  # Map the function to the list

    # Print results
    for result in results:
        print(f"Result: {result}")
