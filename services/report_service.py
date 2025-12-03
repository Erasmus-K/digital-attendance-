from config.database import SessionLocal
from models.student import Student

def register_student(admission_no, full_name, course_id):
    db = SessionLocal()
    try:
        student = Student(admission_no=admission_no, full_name=full_name, course_id=course_id)
        db.add(student)
        db.commit()
        return True, "Student registered successfully"
    except Exception as e:
        return False, str(e)
    finally:
        db.close()
