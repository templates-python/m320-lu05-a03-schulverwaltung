import pytest
from grade import Grade


class TestGrade:

    """
    Test des Konstruktors auf gültigen Notenwert.
    """
    def test_grade_initial_value_OK(self):
        grade = Grade(4.0, '3.3.33')
        assert grade.value == 4.0

    """
    Test des Konstruktors auf zu kleinen Notenwert.
    """
    def test_grade_initial_value_to_low(self):
        grade = Grade(-1.0, '3.3.35')
        assert grade.value == -1.0

    """
    Test des Konstruktors auf zu grossen Notenwert.
    """
    def test_grade_initial_value_to_high(self):
        grade = Grade(7.0, '3.3.35')
        assert grade.value == -1.0

    """
    Test des Konstruktors auf Datum.
    """
    def test_grade_date_set(self):
        grade = Grade(3.0, '3.3.33')
        assert grade.date == '3.3.33'