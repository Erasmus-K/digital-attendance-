from services.student_service import register_student
from services.attendance_service import record_attendance
from services.report_service import student_report

def start_menu():
    while True:
        print("\n=== Digital Attendance System ===")
        print("1. Register student")
        print("2. Record attendance")
        print("3. View report")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admission = input("Admission number: ")
            name = input("Full name: ")
            course = input("Course ID: ")
            ok, msg = register_student(admission, name, course)
            print(msg)

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
