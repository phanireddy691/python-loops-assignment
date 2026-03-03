def calculate_grade(*scores, **adjustments):
    # 1. Calculate the average of test scores
    if not scores:
        average = 0
    else:
        average = sum(scores) / len(scores)
    
    # 2. Calculate the sum of all bonus adjustments
    bonus_sum = sum(adjustments.values())
    
    # 3. Final Logic: Average of scores + sum of adjustments
    final_grade = average + bonus_sum
    
    return final_grade

# --- Tasks ---

# 1. Student with scores: 85, 90, 78 (no bonus)
grade1 = calculate_grade(85, 90, 78)
print(f"Final Grade: {grade1:.2f}%")

# 2. Student with scores: 70, 65, 80 (with attendance=5, project=10 bonus)
grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
print(f"Final Grade: {grade2:.2f}%")