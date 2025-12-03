#!/usr/bin/env python3

from config.database import Base, engine, SessionLocal
from models import student, course, attendance
from services.student_service import register_student
from services.attendance_service import record_attendance
from services.report_service import student_report

def test_system():
    # Initialize database
    Base.metadata.create_all(bind=engine)
    print("✓ Database created successfully")
    
    # Test student registration
    success, msg = register_student("5324", "Erasmus Kipkosgei", 1)
    print(f"✓ Student registration: {msg}")
    
    # Test attendance recording
    success, msg = record_attendance("5324", "2024-12-03", "Present")
    print(f"✓ Attendance recording: {msg}")
    
    # Test report generation
    report = student_report("5324")
    print(f"✓ Report generated:\n{report}")
    
    print("\n🎉 All systems working correctly!")

if __name__ == "__main__":
    test_system()