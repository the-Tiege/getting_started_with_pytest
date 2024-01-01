"""
Classroom Management Module

This module defines classes for managing a classroom, including custom exception classes,
a base class for a person, and specific classes for teachers and students.

Classes:
- TooManyStudents: Custom exception class to represent an error when attempting to add
  more than 10 students to a classroom.
- Person: A base class representing a generic person with a name attribute.
- Teacher: A class representing a teacher, inheriting from the Person class.
- Student: A class representing a student, inheriting from the Person class.
- Classroom: A class representing a classroom with a teacher, students, and a course title.
  Methods include adding students, removing students, and changing the teacher.

Example Usage:
Create instances of Teacher, Student, and Classroom

teacher_instance = Teacher(name="Mr. Smith")
student_instance = Student(name="Alice")
classroom_instance = Classroom(teacher=teacher_instance, students=[], course_title="Mathematics")
Add students to the classroom

classroom_instance.add_student(student_instance)
Remove a student from the classroom

classroom_instance.remove_student(name="Alice")
Change the teacher of the classroom

new_teacher_instance = Teacher(name="Ms. Johnson")
classroom_instance.change_teacher(new_teacher=new_teacher_instance)

Note: The Classroom class has a limitation on the number of students (up to 10),
and attempting to add more students than allowed will raise the TooManyStudents exception.
"""

class TooManyStudents(Exception):
    """
    Custom exception class to represent an error when attempting to
    add more than 10 students to a classroom.
    """


class Person:
    """
    A base class representing a generic person.

    Attributes:
    - name: str 
            The name of the person.
    """

    def __init__(self, name):
        """
        Initialize a Person instance with a given name.

        Parameters:
        - name: str 
                The name of the person.
        """
        self.name = name


class Teacher(Person):
    """
    A class representing a teacher, inheriting from the Person class.
    """


class Student(Person):
    """
    A class representing a student, inheriting from the Person class.
    """


class Classroom:
    """
    A class representing a classroom with a teacher, students, and a course title.

    Attributes:
    - teacher: Teacher
               The teacher of the classroom.
    - students: list
                A list of Student objects in the classroom.
    - course_title: str
                    The title of the course taught in the classroom.

    Methods:
    - add_student(student): Adds a student to the classroom if the number
                            of students is less than or equal to 10.
      Raises TooManyStudents exception otherwise.
    - remove_student(name): Removes a student from the classroom by name.
    - change_teacher(new_teacher): Changes the teacher of the classroom to a new Teacher object.
    """

    def __init__(self, teacher: Teacher, students: list, course_title: str) -> None:
        """
        Initialize a Classroom instance with a given teacher, list of students, and course title.

        Parameters:
        - teacher: Teacher
                   The teacher of the classroom.
        - students: list
                    A list of Student objects in the classroom.
        - course_title: str
                        The title of the course taught in the classroom.
        """
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student: Student) -> None:
        """
        Add a student to the classroom if the number of students is less than or equal to 10.
        Raises TooManyStudents exception otherwise.

        Parameters:
        - student: Student
                   The student to be added to the classroom.
        """
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudents

    def remove_student(self, name: str) -> None:
        """
        Remove a student from the classroom by name.

        Parameters:
        - name: str 
                The name of the student to be removed.
        """
        for student in self.students:
            if student == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher: Teacher):
        """
        Change the teacher of the classroom to a new Teacher object.

        Parameters:
        - new_teacher: Teacher
                       The new teacher for the classroom.
        """
        self.teacher = new_teacher
