"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    pass

class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__status = "Active"

    def get_id(self):
        return self.__student_id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_status(self, status):
        allowed_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        if status in allowed_statuses:
            self.__status = status

    def get_status(self):
        return self.__status


if __name__ == '__main__':
    student = Student("John Doe", 12345)

    print(student.get_id())
    print(student.get_name())
    print(student.get_status())

    student.set_name("Jane Doe")
    print(student.get_name())

    student.set_status("Finished")
    print(student.get_status())

    student.set_status("Graduated")
    print(student.get_status())
