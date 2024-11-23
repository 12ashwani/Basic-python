import threading
import time

def print_number():
    for i in range(1, 5):
        print(f'Number: {i}')
        time.sleep(0.5)  # Simulate a delay

def print_letter():
    for letter in 'abcde':
        print(f'Letter: {letter}')
        time.sleep(0.5)  # Simulate a delay

# Measure execution time
start_time = time.time()

# Create threads
thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_letter)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

finished_time = time.time()

print(f"Execution time with threading: {finished_time - start_time:.2f} seconds")
