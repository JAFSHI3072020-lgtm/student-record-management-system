def add_student(students, student):
    for s in students:
        if s["roll"] == student["roll"]:
            return False
    students.append(student)
    return True


def remove_student(students, roll):
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            return True
    return False


def search_student(students, term):
    results = []
    term = term.lower()

    for student in students:
        if (term in student["name"].lower()
                or term in student["email"].lower()
                or term == str(student["roll"])):
            results.append(student)

    return results
