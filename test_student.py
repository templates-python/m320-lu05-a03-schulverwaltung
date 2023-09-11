import pytest
from classreport import ClassReport
from subject import Subject
from grade import Grade
from student import Student


class TestStudent:

    @pytest.fixture
    def class_report(self):
        return ClassReport()

    @pytest.fixture
    def student(self, class_report):
        return Student(self, 'Konrad', class_report)

    @pytest.fixture
    def subject(self):
        return Subject('Mathe')

    """
    Test der Initialisierung mit Name und Report
    """
    def test_initialisation(self, student, class_report):
        assert student.name == 'Konrad'
