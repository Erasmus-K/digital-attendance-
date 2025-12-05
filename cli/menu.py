from services.student_service import register_student
from services.attendance_service import record_attendance
from services.report_service import student_report
from config.database import SessionLocal
from models.course import Course

def show_courses():
    db = SessionLocal()
    try:
        courses = db.query(Course).all()
        print("\nAvailable Courses:")
        for course in courses:
            print(f"  {course.id}. {course.name}")
        print()
    finally:
        db.close()

def start_menu():
    while True:
        print("\n=== Digital Attendance System ===")
        print("1. Register student")
        print("2. Record attendance")
        print("3. View report")
        print("4. Show courses")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_courses()
            admission = input("Admission number: ")
            name = input("Full name: ")
            course = input("Course ID: ")
            ok, msg = register_student(admission, name, course)
            print(msg)
            
        elif choice == "4":
            show_courses()

        elif choice == "2":
            adm = input("Admission number: ")
            date = input("Date (YYYY-MM-DD): ")
            status = input("Status (Present/Absent): ")
            ok, msg = record_attendance(adm, date, status)
            print(msg)

        elif choice == "3":
            adm = input("Admission number: ")
            print(student_report(adm))

        elif choice == "0":
            break

        else:
            print("Invalid choice!")
