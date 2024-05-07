from sqlalchemy.orm import sessionmaker
from main import Student, Group, Teacher, Subject, Grade
from sqlalchemy import func, desc

# Функція для підключення до бази даних
def connect_db(engine):
    Session = sessionmaker(bind=engine)
    return Session()

# Запити

def select_1(session):
    # Знайти 5 студентів з найбільшим середнім балом з усіх предметів.
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, subject_name):
    # Знайти студента із найвищим середнім балом з певного предмета.
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Grade).join(Subject).filter(Subject.name == subject_name) \
                  .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(session, subject_name):
    # Знайти середній бал у групах з певного предмета.
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
                  .join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name) \
                  .group_by(Group.name).all()

def select_4(session):
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(session, teacher_id):
    # Знайти які курси читає певний викладач.
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(session, group_id):
    # Знайти список студентів у певній групі.
    return session.query(Student.fullname).filter(Student.group_id == group_id).all()

def select_7(session, group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    return session.query(Student.fullname, Grade.grade).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(session, teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    return session.query(func.round(func.avg(Grade.grade), 2)).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(session, student_id):
    # Знайти список курсів, які відвідує певний студент.
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).distinct().all()

def select_10(session, student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).distinct().all()