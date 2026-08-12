import time
import random

def performance_optimized_function(data):
    start_time = time.time()
    results = []
    for item in data:
        process_time = random.uniform(0.1, 0.5)
        time.sleep(process_time)  # Simulate processing time
        results.append(item ** 2)  # Example processing: squaring the item
    end_time = time.time()
    print(f"Processing time: {end_time - start_time} seconds")
    return results

if __name__ == '__main__':
    sample_data = list(range(10))
    output = performance_optimized_function(sample_data)
    print(output)