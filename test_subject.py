import pytest
from subject import Subject
from grade import Grade


class TestSubject:

    @pytest.fixture
    def subject(self):
        return Subject('Mathe')

    def test_initialisation(self, subject):
        assert subject.name == 'Mathe'
        assert subject.size == 0

    def test_grade_added_size(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.size == 1

    def test_grade_value(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.get_value(0) == 3.0

    def test_grade_average(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.get_average() == 3.0

    def test_multi_added_size(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.size == 3

    def test_multi_grade_value(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.get_value(0) == 3.0
        assert subject.get_value(1) == 5.0
        assert subject.get_value(2) == 4.0

    def test_average(self, subject):
        assert subject.get_average() == 4.0

    def test_max_grades(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        subject.add_grade(Grade(1.0, '1.2.44'))
        subject.add_grade(Grade(2.0, '1.2.55'))
        assert subject.size == 4
