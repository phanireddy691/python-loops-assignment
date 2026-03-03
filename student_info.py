name = input("Enter student name : ")
math_marks = int(input("Enter maths marks: "))
science_marks =int(input("Enter Science marks: "))
english_marks= int(input("Enter English marks: "))

scores = [math_marks,science_marks,english_marks]
for marks in scores:
        if marks < 0 or marks > 100:
            print("Invalid marks entered")
            exit()

total_score = int(math_marks + science_marks + english_marks)
average_score = float(total_score/3)


status = "pass"
for result in scores:
    if result <= 40:
      status = "Fail"
      break

if average_score >= 75:
    grade = "A"
elif average_score >= 60 and average_score <= 75:
    grade = "B"
elif average_score >= 40 and average_score <= 60:
    grade = "C"
            

print(f"\nStudent Name: {name}")
print(f"Total marks: {total_score}")
print(f"Percentage: {average_score:.2f}")
print(f"Status: {status}")
print(f"Grade: {grade}")



