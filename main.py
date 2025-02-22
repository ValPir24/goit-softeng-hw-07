from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = orm.declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", back_populates="group")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    subjects = relationship("Subject", back_populates="teacher")

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(Date)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

# Для створення бази даних та зв'язків між таблицями
engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)
