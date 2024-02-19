# Import pytest and the StudentsInMLOps class from main.py
import pytest
from main import StudentsInMLOps

def test_enroll_students():
    # Create an instance of the StudentsInMLOps class
    students_in_mlops = StudentsInMLOps()
    # Enroll 5 students
    students_in_mlops.enrollStudents(5)
    # Check if the total students count is correct
    assert students_in_mlops.getTotalStrength() == 5

def test_drop_students():
    students_in_mlops = StudentsInMLOps()
    # Initially enroll 5 students
    students_in_mlops.enrollStudents(5)
    # Drop 2 students
    students_in_mlops.dropStudents(2)
    # Check if the total students count is correct after dropping students
    assert students_in_mlops.getTotalStrength() == 3

def test_total_strength():
    students_in_mlops = StudentsInMLOps()
    # Enroll 5 students
    students_in_mlops.enrollStudents(5)
    # Check if the getTotalStrength method returns the correct total number of students
    assert students_in_mlops.getTotalStrength() == 5

def test_class_name():
    students_in_mlops = StudentsInMLOps()
    # Check if the getClassName method returns the correct class name
    assert students_in_mlops.getClassName() == "Students in MLOps"

def test_drop_students_not_negative():
    students_in_mlops = StudentsInMLOps()
    # Drop 2 students without enrolling anyone first
    students_in_mlops.dropStudents(2)
    # Ensure the total number of students does not go negative
    assert students_in_mlops.getTotalStrength() == 0
