📘 Digital Class Attendance Application (CLI + ORM)

Developer: Erasmus Kipkosgei

A Python Phase 3 Project | SQLAlchemy ORM | Pipenv | CLI Menu System

📌 Project Overview

The Digital Class Attendance Application is a Python-based Command Line Interface (CLI) system designed for registering students, managing course assignments, recording attendance, and generating reports.

This project adheres to Phase 3 requirements:

✔ A real-world problem solved with a CLI
✔ SQLAlchemy ORM with 3+ related tables
✔ Well-maintained Pipenv virtual environment
✔ Clean, modular package structure
✔ Use of lists, dicts, tuples
✔ Best practices in Python project organization

The system is simple enough for beginners but structured professionally for scalability.

 Learning Goals (Phase 3 Requirements)

This project demonstrates proficiency in:

1. CLI Application Development

Menu-driven user interaction

Input validation

Clear separation of logic and interface

2. SQLAlchemy ORM

Creating declarative models

3+ related tables (Students, Courses, Attendance)

Foreign key relationships

Sessions & CRUD operations

3. Pipenv Environment Management

Creating isolated environments

Installing dependencies with Pipenv

Consistent dependency management

4. Python Package Structure

Organized modules under models/, services/, cli/, and config/

Separation of concerns

Readability and maintainability

5. Python Data Structures

Lists for record display

Dictionaries for mapping

Tuples returned from CRUD operations

 Project Folder Structure
digital_attendance_app/
│
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── app.py                        # Entry point (initializes DB + starts CLI)
│
├── config/
│   └── database.py               # SQLAlchemy engine, session, Base
│
├── models/
│   ├── __init__.py
│   ├── student.py                # Student ORM model
│   ├── course.py                 # Course ORM model
│   └── attendance.py             # Attendance ORM model
│
├── services/
│   ├── __init__.py
│   ├── student_service.py        # CRUD logic for students
│   ├── attendance_service.py     # Attendance handling logic
│   └── report_service.py         # Reporting logic
│
└── cli/
    ├── __init__.py
    └── menu.py                   # CLI menu and user interaction logic


This structure ensures clean, scalable, and testable code.

    Installation & Setup
✔ 1. Install Python 3.8+
✔ 2. Create a Pipenv Environment

Inside your project folder:

pipenv --python 3.10

✔ 3. Install Dependencies
pipenv install sqlalchemy tabulate

✔ 4. Activate Environment
pipenv shell

     Database Setup

The database file attendance.db is created automatically using SQLAlchemy when you run:

python app.py


The tables:

1. students
Field	Type	Description
id	Integer (PK)	Unique student ID
admission_no	String	Unique admission number
full_name	String	Full student name
course_id	Integer (FK)	Course assigned
2. courses
Field	Type
id	Integer (PK)
name	String (unique)
3. attendance
Field	Type
id	Integer (PK)
date	String (YYYY-MM-DD)
status	“Present” / “Absent”
student_id	FK -> students.id
     How to Run the Application
python app.py


After starting, you will see a menu like:

=== Digital Attendance System ===
1. Register student
2. Record attendance
3. View report
0. Exit

     Features / How It Works
     1. Register Students

Assign admission number

Assign full name

Assign a course ID

Saved into the database

    2. Record Attendance

Choose student by admission number

Provide date (YYYY-MM-DD)

Mark Present/Absent

    3. Generate Reports

Student attendance summary

Date-based attendance list

Total Present vs Absent

    4. Search & List

View all students

Search by name/course/admission number

    Example Reports
Student Attendance Report
Report for John Doe (ADM001)
--------------------------------------------------
2025-01-12 : Present
2025-01-13 : Absent
--------------------------------------------------
Total: 2 | Present: 1 | Absent: 1

Date Attendance Report
Attendance for 2025-01-12
----------------------------------------
5324 - Erasmus kipkosgei : Present
18354 - Brenda Jebet : Absent
----------------------------------------
Total students recorded: 2

🧪 Technologies Used
Tech	Purpose
Python	Language
SQLAlchemy ORM	Database layer
Pipenv	Virtual environment & dependency management
SQLite	Database
Tabulate	Formatting tables in CLI

