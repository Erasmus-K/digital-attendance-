#!/usr/bin/env python3

from config.database import Base, engine, SessionLocal
from models import student, course, attendance
from models.course import Course

def setup_courses():
    # Create all tables first
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created")
    
    db = SessionLocal()
    try:
        # Check if courses already exist
        existing_courses = db.query(Course).count()
        if existing_courses > 0:
            print(f"Found {existing_courses} courses already in database")
            return
        
        # Add sample courses
        courses = [
            Course(id=1, name="Computer Science"),
            Course(id=2, name="Software Engineering"),
            Course(id=3, name="Data Science"),
            Course(id=4, name="Web Development"),
            Course(id=5, name="Mobile Development"),
            Course(id=6, name="Cybersecurity")
        ]
        
        for course in courses:
            db.add(course)
        
        db.commit()
        print("✓ Sample courses added successfully!")
        
        # Display added courses
        all_courses = db.query(Course).all()
        print("\nAvailable Courses:")
        for course in all_courses:
            print(f"ID: {course.id} - {course.name}")
            
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    setup_courses()