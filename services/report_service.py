from config.database import SessionLocal
from models.student import Student
from models.attendance import Attendance
from tabulate import tabulate

def student_report(admission_no):
    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.admission_no == admission_no).first()
        if not student:
            return "Student not found"
        
        attendance_records = db.query(Attendance).filter(Attendance.student_id == student.id).all()
        
        if not attendance_records:
            return f"No attendance records found for {student.full_name}"
        
        headers = ["Date", "Status"]
        data = [[record.date, record.status] for record in attendance_records]
        
        report = f"\nAttendance Report for {student.full_name} ({student.admission_no})\n"
        report += tabulate(data, headers=headers, tablefmt="grid")
        
        present_count = sum(1 for record in attendance_records if record.status.lower() == "present")
        total_count = len(attendance_records)
        attendance_rate = (present_count / total_count) * 100 if total_count > 0 else 0
        
        report += f"\n\nSummary: {present_count}/{total_count} classes attended ({attendance_rate:.1f}%)"
        
        return report
    except Exception as e:
        return f"Error generating report: {str(e)}"
    finally:
        db.close()
