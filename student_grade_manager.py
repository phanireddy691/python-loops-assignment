students = [
    "Alice,85",
    "Bob,92",
    "Charlie,78",
    "Diana,95"
]

with open("students.txt", "w") as file:
    for record in students:
        file.write(record + "\n")

print("data written to students.txt succesfully")
    
# No file.close() needed here; 'with' does it for you!


#Task 2

with open("students.txt", "r") as file:
    for line in file:
        name,score = line.strip().split(",")
        print(f"student: {name}, Score : {score}")


#Task 3

with open("students.txt", "a") as file:
    file.write("Eve,88\n")

with open("Activity.log", "w") as log_file:
    log_file.write("Added nrw student: Eve")
        

