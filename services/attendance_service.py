from config.database import SessionLocal
from models.student import Student
from models.attendance import Attendance

def record_attendance(admission_no, date, status):
    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.admission_no == admission_no).first()
        if not student:
            return False, "Student not found"
        
        attendance = Attendance(date=date, status=status, student_id=student.id)
        db.add(attendance)
        db.commit()
        return True, f"Attendance recorded for {student.full_name}"
    except Exception as e:
        return False, str(e)
    finally:
        db.close()