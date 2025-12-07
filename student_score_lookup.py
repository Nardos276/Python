scores = {"John": 85, "Sara": 92, "Fraol": 78}
name = input("Enter the student name: ")
try:
    print(f"{name}'s score is {scores[name]}")
except KeyError:
    print("Student not found!")
