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


#Task---> 3
import time
arr = np.arange(1, 50001)
lis = list(range(1, 50001))

start_np = time.time()
numpy_sum = np.sum(arr)
end_np = time.time()
numpy_time = start_np - end_np


start_py = time.time()
python_sum = sum(lis)
end_np = time.time()
python_time = start_np - end_np

speed_factor = python_time / numpy_time

print(f"numpy sum: {numpy_sum}")
print(f"Python sum: {python_sum}")
print(f"Numpy time: {numpy_time:.4f}")
print(f"Python time: {python_time:.4f}")
print(f"Numpy is {speed_factor:.1f}x faster")
