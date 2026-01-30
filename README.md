# student-record-management-system
 student-record-management-system

This project is a Command-Line Interface (CLI) based Student Record Management System developed using Python.  
The application runs entirely in the terminal and does not use any graphical user interface or external libraries.

---

## Features

- Add new student records
- Prevent duplicate roll numbers
- View all stored student records
- Search students by name, email, or roll number
- Remove student records using roll number with confirmation
- Automatically save student data to a file
- Load saved records when the program starts
- Display meaningful error messages for invalid inputs

---

## Student Information Fields

- Student Name  
- Roll Number  
- Email Address  
- Department  

---

## Project Structure

student_record_system/
│
├── main.py # Main program and menu system
├── student.py # Student-related operations
├── file_handler.py # File handling (read/write)
├── utils.py # Input validation functions
└── students.csv # Data file (auto-created)


---

## How to Run the Project

1. Ensure Python is installed on your system.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the following command:

```bash
python main.py
Menu Options
1. Add Student
2. View Students
3. Search Student
4. Remove Student
5. Exit
Technologies Used
Python (Core Python only)

Command Line Interface (CLI)

Notes
No external libraries are used.

The application runs completely in the terminal.

Student data is stored in a CSV file.
