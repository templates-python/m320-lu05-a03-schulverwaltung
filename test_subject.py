import pytest
from subject import Subject
from grade import Grade


class TestSubject:

    @pytest.fixture
    def subject(self):
        return Subject('Mathe')

    @pytest.fixture
    def grade(self):
        return Grade( 4.0, '1.2.33')

    """
    Test mit leerem Subject.
    """
    def test_empty_subject(self, subject):
        assert subject.name == 'Mathe'
        assert subject.size == 0

    """
    Test mit einem Element.
    """
    def test_single_grade_added(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.size == 1

    """
      Test mit 4 Elementen.
    """
    def test_multi_grade_added(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.size == 3

    """
        Test mit mehr als 4 Elementen.
    """
    def test_max_grades_added(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        subject.add_grade(Grade(1.0, '1.2.44'))
        subject.add_grade(Grade(2.0, '1.2.55'))
        assert subject.size == 4

    """
    Test bei Zugriff mit gültigem Index.
    """
    def test_get_grade_valid(self, subject, grade):
        subject.add_grade(grade)
        assert subject.take_value(0) == grade.value
        assert subject.take_date(0) == grade.date

    """
    Test bei Zugriff mit ungültigem Index
    """
    def test_get_grade_invalid(self, subject, grade):
        subject.add_grade(grade)
        assert subject.take_value(1) == 0
        assert subject.take_date(1) == None

    """
    Test der Methoden get_value und get_date auf deren Wertrückgabe.
    """
    def test_single_grade(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.take_value(0) == 3.0
        assert subject.take_date(0) == '1.2.33'

    """
    Test der Inhalte bei mehreren zugefügten Noten.
    """
    def test_multi_grade(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.take_value(0) == 3.0
        assert subject.take_value(1) == 5.0
        assert subject.take_value(2) == 4.0
        assert subject.take_date(0) == '1.2.33'
        assert subject.take_date(1) == '1.2.44'
        assert subject.take_date(2) == '1.2.55'



    """
    Test des Mittelwertes bei fehlendem Noteneintrag.
    """
    def test_average_without_grade(self, subject):
        assert subject.average == 0

    """
    Test des Mittelwertes bei einer Note.
    """
    def test_single_grade_average(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.average == 3.0

    """
    Test des Mittelwertes bei mehreren zugefügten Noten.
    """
    def test_average(self, subject):
        subject.add_grade(Grade(2.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        subject.add_grade(Grade(1.0, '1.2.44'))
        assert subject.average == 3.0