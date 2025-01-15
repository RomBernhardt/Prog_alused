"""School class which stores information about courses and students."""


class School:
    pass
from student import Student
from course import Course

class School:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.courses = []
        self.student_id_counter = 1

    def add_student(self, student: Student):
        if student not in self.students:
            student.set_id(self.student_id_counter)
            self.students.append(student)
            self.student_id_counter += 1

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)

"""Student class with student name and grades."""


class Student:
    pass
from course import Course

class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def get_grades(self) -> list:
        return self.grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self) -> str:
        return self.name

    def add_grade(self, course: Course, grade: int):
        self.grades.append((course, grade))

"""Course class with name and grades."""


class Course:
    pass
from student import Student

class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def get_grades(self):
        return self.grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def add_grade(self, student: Student, grade: int):
        self.grades.append((student, grade))

    def __repr__(self):
        return self.name
