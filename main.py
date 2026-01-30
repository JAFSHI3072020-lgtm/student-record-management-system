from student import add_student, remove_student, search_student
from file_handler import load_students, save_students
from utils import get_non_empty_string, get_valid_roll, get_email


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n===== All Students =====")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name : {s['name']}")
        print(f"   Roll : {s['roll']}")
        print(f"   Email : {s['email']}")
        print(f"   Department : {s['department']}")
        print("------------------------")


def menu():
    print("\n=========== MENU ===========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    print("============================")


def main():
    print("Welcome to the Student Record Management System!")
    print("Loading student records from students.csv... Done!")

    students = load_students()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = get_non_empty_string("Enter Student Name: ")
            roll = get_valid_roll("Enter Roll Number: ")
            email = get_email("Enter Email: ")
            dept = get_non_empty_string("Enter Department: ")

            student = {
                "name": name,
                "roll": roll,
                "email": email,
                "department": dept
            }

            if add_student(students, student):
                save_students(students)
                print("Student record added successfully!")
            else:
                print("Error: Roll number already exists for another student.")

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            term = input("Enter search term (name/email/roll): ")
            results = search_student(students, term)

            if results:
                print("\nSearch Result:")
                display_students(results)
            else:
                print("No matching student found.")

        elif choice == "4":
            roll = get_valid_roll("Enter the roll number of the student to delete: ")
            confirm = input(f"Are you sure you want to delete student with roll {roll}? (y/n): ")

            if confirm.lower() == "y":
                if remove_student(students, roll):
                    save_students(students)
                    print("Student record deleted successfully!")
                else:
                    print("Student not found.")

        elif choice == "5":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
