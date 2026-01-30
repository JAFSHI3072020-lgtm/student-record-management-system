import os

FILE_NAME = "students.csv"


def load_students():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, roll, email, dept = line.strip().split(",")
            students.append({
                "name": name,
                "roll": int(roll),
                "email": email,
                "department": dept
            })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['roll']},{s['email']},{s['department']}\n")
