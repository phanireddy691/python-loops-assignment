#Task--->

import numpy as np

np.random.seed(42)

scores = np.random.randint(50,101,(5,4))
print(f"Original scores:\n {scores}")
print(f"3rd student in 2nd subject: {scores[2,1]}")
print(f"last 2 students: {scores[-2:]}")
print(f"first 3 students in subjects 2 and 3 only: {scores[:3, 1:3]}")


#Task ---> 2

#column_wise_mean, rounded to 2

column_wise_mean = np.round(scores.mean(axis = 0),2)
print(f"column wise mean: {column_wise_mean}")

#Add a curve using broadcasting
curve_values = [5, 3, 7, 2]
curved_scores = scores + curve_values

#ensure no scores exedding 100 clipping

curved_scores = np.clip(curved_scores, 0, 100)
print(f"Curved scored with clipping: {curved_scores}")

#row_wise_max
row_wise_max = curved_scores.max(axis = 1)
print(f"row wise max: {row_wise_max}")

#Task----> 3

#normalization row min row max

row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)
normalized_array = (curved_scores - row_min) / (row_max - row_min)

print(f"Normalized array: {normalized_array}")

#student_index(row) and subject_index(column) of single highest value across the array

max_value = np.max(normalized_array)

rows, cols = np.where(normalized_array == max_value)

student_index = rows[0]
subject_index = cols[0]

print(f"Highest values at: Student {student_index}, Subject {subject_index} ")

#scores above 90

scores_above_90 = curved_scores[curved_scores > 90]
print(f"Scores strictly above 90: {scores_above_90}")


