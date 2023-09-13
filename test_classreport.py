import pytest
from classreport import ClassReport
from subject import Subject
from grade import Grade


class TestClassReport:

    @pytest.fixture
    def report(self):
        return ClassReport()

    @pytest.fixture
    def subject(self):
        return Subject('Mathe')

    """
    Test eines leeren Reports
    """
    def test_empty_report(self, report):
        assert report.size == 0

    """
    Test mit einem Element.
    """
    def test_single_subject_added(self, report):
        report.add_subject(Subject('Mathe'))
        assert report.size == 1

    """
    Test mit 3 Elementen
    """
    def test_multi_subject_added(self, report):
        report.add_subject(Subject('Mathe'))
        report.add_subject(Subject('Deutsch'))
        report.add_subject(Subject('Sport'))
        assert report.size == 3

    """
    Test mit mehr als 3 Elementen
    """
    def test_max_subjects_added(self, report):
        report.add_subject(Subject('Mathe'))
        report.add_subject(Subject('Deutsch'))
        report.add_subject(Subject('Sport'))
        report.add_subject(Subject('M&T'))
        assert report.size == 3

    """
    Test bei Zugriff mit gültigem Index.
    """
    def test_get_subject_valid(self, report, subject):
        report.add_subject(subject)
        assert report.take_subject(0) is subject

    """
    Test bei Zugriff mit ungültigem Index
    """
    def test_get_subject_invalid(self, report, subject):
        report.add_subject(subject)
        assert report.take_subject(4) == None

