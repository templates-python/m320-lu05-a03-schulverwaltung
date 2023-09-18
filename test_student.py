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
    def mia(self, class_report):
        return Student('Mia', class_report)

    @pytest.fixture
    def mathe(self):
        return Subject('Mathe')

    """
    Test der Initialisierung und der getter
    """
    def test_initialisation(self, mia, class_report):
        assert mia.name == 'Mia'
        assert mia.school_class is None
        assert mia.report is class_report

    """
    Test der Zuweisung der (eigenen) Student-Referenz an ein ClassReport-Objekt
    """
    def test_relationship_to_classreport(self, mia, class_report):
        assert mia.report.student is mia
