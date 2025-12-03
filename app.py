from config.database import Base, engine
from models import student, course, attendance
from cli.menu import start_menu

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    start_menu()
