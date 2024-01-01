"""
Test Module for School Module

This module contains test cases for the 'Classroom', 'Teacher', and 'Student' classes in the 'school' module.
The tests cover functionality related to changing teachers, adding students, removing students,
and handling the 'TooManyStudents' exception.

Test Fixtures:
- empty_classroom: A fixture providing an empty 'Classroom' instance for testing purposes.
- full_classroom: A fixture providing a 'Classroom' instance with 10 students for testing purposes.

Test Functions:
- test_change_teacher(full_classroom, new_teacher_name): Test case for changing the teacher of a 'Classroom'.
- test_add_student(empty_classroom, num_students): Test case for adding students to an empty 'Classroom'.
- test_remove_student(full_classroom): Test case for removing a student from a 'Classroom'.
- test_too_many_students_exception(): Test case for handling the 'TooManyStudents' exception.

Example Usage:

Run the tests using pytest:
$ pytest test_school.py

Note: This module assumes the availability of the 'school' module and uses pytest for testing.
"""
import pytest

from getting_started_pytest.school import (Classroom, Student, Teacher,
                                           TooManyStudents)


@pytest.fixture
def empty_classroom():
    """
    Fixture providing an empty 'Classroom' instance for testing purposes.

    Returns:
    Classroom: An empty 'Classroom' instance.
    """
    teacher = Teacher("Professor Snape")
    students = []
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


@pytest.fixture
def full_classroom():
    """
    Fixture providing a 'Classroom' instance with 10 students for testing purposes.

    Returns:
    Classroom: A 'Classroom' instance with 10 students.
    """
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student{i}") for i in range(10)]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


@pytest.mark.parametrize("new_teacher_name", ["Professor McGonagall", "Professor Dumbledore"])
def test_change_teacher(full_classroom, new_teacher_name):
    """
    Test case for changing the teacher of a 'Classroom'.

    Parameters:
    - full_classroom: Classroom
                      A 'Classroom' instance with 10 students for testing purposes.
    - new_teacher_name: str
                        The name of the new teacher.
    """
    new_teacher = Teacher(new_teacher_name)
    full_classroom.change_teacher(new_teacher)
    assert full_classroom.teacher == new_teacher


@pytest.mark.parametrize("num_students", [17, 15, 12, 120])
def test_add_student(empty_classroom, num_students):
    """
    Test case for adding students to an empty 'Classroom' and handling 'TooManyStudents' exception.

    Parameters:
    - empty_classroom: Classroom
                      An empty 'Classroom' instance for testing purposes.
    - num_students: int
                    The number of students to add to the classroom.
    """
    new_students = [Student(f"New Student {i}") for i in range(num_students)]

    with pytest.raises(TooManyStudents):
        for student in new_students:
            empty_classroom.add_student(student)
            assert student in empty_classroom.students


def test_remove_student(full_classroom):
    """
    Test case for removing a student from a 'Classroom'.

    Parameters:
    - full_classroom: Classroom
                      A 'Classroom' instance with 10 students for testing purposes.
    """
    student_to_remove = full_classroom.students[0]
    full_classroom.remove_student(student_to_remove)
    assert student_to_remove not in full_classroom.students


def test_too_many_students_exception():
    """
    Test case for handling the 'TooManyStudents' exception.
    Verifies that attempting to create a 'Classroom' with more than 10 students raises the exception.
    """
    with pytest.raises(TooManyStudents):
        teacher = Teacher("Professor Snape")
        students = [Student(f"Student{i}") for i in range(11)]
        course_title = "Potions"
        classroom = Classroom(teacher, students, course_title)
        classroom.add_student(Student("Harry"))
