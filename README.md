# Student Performance Posting System

This system is designed to allow users to manage and track the performance of students across different courses. It uses SQLAlchemy with a SQLite database to store information about students, courses, and grades.

## Features

- Add new students to the system.
- Add new subjects (courses).
- Record grades for students in different subjects.
- View all recorded performances.
- View performances for a specific student.

## Installation

Before you can run this system, you'll need to install Python and the necessary libraries. Here's how you can set it up:

1. Ensure that you have Python installed on your system.
2. Install SQLAlchemy by running the command:


## How to use
To use the system, follow these steps:

1. Clone or download the repository containing the code.
2. Navigate to the directory containing the code.
3. Run the script using Python:



python student_performance_system.py

Once the script is running, follow the on-screen menu to interact with the system:

Menu:

Add Student
Add Subject
Add Grade
View All Performances
View Performances for a Specific Student
Exit


Choose an option by typing the corresponding number and hitting Enter.

## Database

The system uses a SQLite database called `student_performance.db` to store all data. The database includes three tables:

- `Students`: Contains student information.
- `Courses`: Contains courses information.
- `Grades`: Records the grades of students in different courses.

