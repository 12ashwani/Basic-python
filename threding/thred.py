## what is the multithreding
## Wheen to use the multi threading
### I/O bound task: Task that spend theat more time waiting for 


import threading
import time

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
print_number()
print_letter()
finished_time = time.time()

print(f"Execution time without threading: {finished_time - start_time:.2f} seconds")


