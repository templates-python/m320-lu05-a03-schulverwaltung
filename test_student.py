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
        return Student('Mia', class_report)

    @pytest.fixture
    def mathe(self):
        return Subject('Mathe')

    """
    Test der Initialisierung mit Name und Report
    """
    def test_initialisation(self, student, class_report):
        assert student.name == 'Mia'
        assert student.report is class_report

    """
    Test der Zuweisung der (eigenen) Student-Referenz an ein ClassReport-Objekt
    """
    def test_relationship_to_classreport(self, mia, class_report):
        assert mia.report.size == 0
      #  assert mia.report.student is self


