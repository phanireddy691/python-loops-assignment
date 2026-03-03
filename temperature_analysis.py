# Task---> 1
import numpy as np
temps_celsius = np.array([22,25,28,24,26])
temps_fahrenheit = (temps_celsius *1.8) + 32
average_farenheit = np.mean(temps_fahrenheit)

print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")
print(f"Average: {average_farenheit}")

#Task---> 2

test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"Shape: {test_scores.shape}")
print(f"Total elements: {test_scores.size}")
print(f"Highest score: {np.max(test_scores)}")
print(f"Lowest score: {np.min(test_scores)}")
print(f"Range: {np.ptp(test_scores)}")


import numpy as np
import time

# Create NumPy array and Python list
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

# Time NumPy sum
start = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start

# Time Python sum
start = time.time()
python_sum = sum(python_list)
python_time = time.time() - start

# Calculate speedup
speedup = python_time / numpy_time

print(f"NumPy sum: {numpy_sum}")
print(f"Python sum: {python_sum}")
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")
print(f"NumPy is {speedup:.1f}x faster")
