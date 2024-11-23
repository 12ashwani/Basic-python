from multiprocessing import Process
import time

def square_number():
    for i in range(5):
        time.sleep(1)  # Simulate a delay
        print(f'Square: {i * i}')

def cube_number():
    for i in range(5):
        time.sleep(1.5)  # Simulate a longer delay
        print(f'Cube: {i ** 3}')

if __name__ == '__main__':
    # Create two processes
    p1 = Process(target=square_number)
    p2 = Process(target=cube_number)

    # Measure execution time
    start_time = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    # Calculate elapsed time
    finished_time = time.time() - start_time
    print(f"Execution time: {finished_time:.2f} seconds")
