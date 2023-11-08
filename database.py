import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('student_performance.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Grades (
                student_id INTEGER,
                course_id INTEGER,
                grade INTEGER,
                PRIMARY KEY (student_id, course_id)
            )
        ''')

        self.conn.commit()

    # Add methods for interacting with the database (insert, retrieve, update, delete, etc.)

    def close(self):
        self.conn.close()
