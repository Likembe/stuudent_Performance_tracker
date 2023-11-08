from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy database engine
engine = create_engine('sqlite:///student_performance.db')
Base = declarative_base()

# Define the Student, Course, and Grade models using SQLAlchemy
class Student(Base):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    grades = relationship('Grade', back_populates='student')

class Course(Base):
    __tablename__ = 'Courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    grades = relationship('Grade', back_populates='course')

class Grade(Base):
    __tablename__ = 'Grades'

    student_id = Column(Integer, ForeignKey('Students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('Courses.id'), primary_key=True)
    grade = Column(Integer, nullable=False)

    student = relationship('Student', back_populates='grades')
    course = relationship('Course', back_populates='grades')

# Create the database schema
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

import argparse

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student = Student(name=name, age=age)
    session.add(student)
    session.commit()
    print(f"Added student: {name}")

def add_subject():
    name = input("Enter subject name: ")
    course = Course(name=name)
    session.add(course)
    session.commit()
    print(f"Added subject: {name}")

def add_grade():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter subject ID: "))
    grade = int(input("Enter grade: "))
    grade_obj = Grade(student_id=student_id, course_id=course_id, grade=grade)
    session.add(grade_obj)
    session.commit()
    print(f"Added grade for student ID {student_id} and subject ID {course_id}: {grade}")

def view_all_performances():
    from sqlalchemy.orm import aliased

    student_alias = aliased(Student)
    course_alias = aliased(Course)

    performances = session.query(Student, Course, Grade) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Course, Course.id == Grade.course_id) \
        .all()

    if performances:
        print("All Performances:")
        for student, course, grade in performances:
            print(f"Student: {student.name}, Course: {course.name}, Grade: {grade.grade}")
    else:
        print("No performances found.")


def view_performances_for_student():
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter(Student.id == student_id).first()

    if student:
        performances = session.query(Grade, Course).join(Course).filter(Grade.student_id == student_id).all()
        if performances:
            print(f"Performances for Student ID {student_id}:")
            for grade, course in performances:
                print(f"Course: {course.name}, Grade: {grade.grade}")
        else:
            print(f"No performances found for Student ID {student_id}.")
    else:
        print(f"Student with ID {student_id} not found.")

def main():
    print("\nWelcome to the Student Performance Posting System")
    while True:
        print("Menu:")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Add Grade")
        print("4. View All Performances")
        print("5. View Performances for a Specific Student")
        print("6. Exit")

        choice = input("Choose an option (1/2/3/4/5/6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_subject()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            view_all_performances()
        elif choice == '5':
            view_performances_for_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()