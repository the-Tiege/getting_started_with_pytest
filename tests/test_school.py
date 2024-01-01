import pytest
from getting_started_pytest.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor Snape")
    students = []
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


@pytest.fixture
def full_classroom():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student{i}") for i in range(10)]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)


@pytest.mark.parametrize("new_teacher_name", ["Professor McGonagall", "Professor Dumbledore"])
def test_change_teacher(full_classroom, new_teacher_name):
    new_teacher = Teacher(new_teacher_name)
    full_classroom.change_teacher(new_teacher)
    assert full_classroom.teacher == new_teacher


@pytest.mark.parametrize("num_students", [17, 15, 12, 120])
def test_add_student(empty_classroom, num_students):
    new_students = [Student(f"New Student {i}") for i in range(num_students)]

    with pytest.raises(TooManyStudents):
        for student in new_students:
            empty_classroom.add_student(student)
            assert student in empty_classroom.students


def test_remove_student(full_classroom):
    student_to_remove = full_classroom.students[0]
    full_classroom.remove_student(student_to_remove)
    assert student_to_remove not in full_classroom.students


def test_classroom_instance_of_person(empty_classroom):
    assert isinstance(empty_classroom, Classroom)


def test_too_many_students_exception():
    with pytest.raises(TooManyStudents):
        teacher = Teacher("Professor Snape")
        students = [Student(f"Student{i}") for i in range(11)]
        course_title = "Potions"
        classroom = Classroom(teacher, students, course_title)
        classroom.add_student(Student("Harry"))
