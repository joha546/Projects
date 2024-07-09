from backend import create_app, db
from backend.auth.models import User, Teacher

app = create_app()

with app.app_context():
    # Add a sample student
    student = User(name="John Doe", email="john@example.com", student_id="S12345")
    student.set_password("password123")
    db.session.add(student)

    # Add a sample teacher
    teacher = Teacher(name="Jane Smith", email="jane@example.com", teacher_id="T67890")
    teacher.set_password("password456")
    db.session.add(teacher)

    db.session.commit()
    print("Sample data added to the database.")