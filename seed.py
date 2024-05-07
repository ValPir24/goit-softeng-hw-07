from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Student, Group, Teacher, Subject, Grade
import random

# Ініціалізуємо Faker
fake = Faker()

# З'єднання з базою даних SQLite
engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()

# Функція для генерації випадкових даних і наповнення бази даних
def seed_database(num_students, num_groups, num_subjects, num_teachers, max_grades_per_student):
    # Наповнення таблиці груп
    for _ in range(num_groups):
        group = Group(name=fake.unique.random_element(("Group A", "Group B", "Group C")))
        session.add(group)

    # Наповнення таблиці викладачів
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        session.add(teacher)

    # Наповнення таблиці предметів
    for _ in range(num_subjects):
        teacher_id = random.randint(1, num_teachers)
        subject = Subject(name=fake.word(), teacher_id=teacher_id)
        session.add(subject)

    # Наповнення таблиці студентів та оцінок
    for _ in range(num_students):
        group_id = random.randint(1, num_groups)
        student = Student(name=fake.name(), group_id=group_id)
        session.add(student)
        for _ in range(random.randint(1, max_grades_per_student)):
            subject_id = random.randint(1, num_subjects)
            grade = random.randint(60, 100)  # Випадкові оцінки від 60 до 100
            date = fake.date_this_year()
            grade = Grade(student_id=student.id, subject_id=subject_id, grade=grade, date=date)
            session.add(grade)

# Генерація даних
seed_database(50, 3, 8, 5, 20)

# Збереження змін у базі даних
session.commit()

# Закриваємо сесію
session.close()
