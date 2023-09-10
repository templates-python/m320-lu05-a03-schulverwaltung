import pytest
from subject import Subject
from grade import Grade


class TestSubject:

    @pytest.fixture
    def subject(self):
        return Subject('Mathe')

    """ 
    Test des Konstruktors und der Methoden get_name und get_size.
    """
    def test_initialisation(self, subject):
        assert subject.name == 'Mathe'
        assert subject.size == 0

    """
    Test der add_grade und der get_size Methoden mit einem Notenwert.
    """
    def test_single_grade_added_size(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.size == 1

    """
    Test des Index bei get_value und get_date Methoden.
    """
    def test_grade_index(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.get_value(1) == 0
        assert subject.get_date(1) == None

    """
    Test der Methoden get_value und get_date auf deren Wertrückgabe.
    """
    def test_single_grade(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.get_value(0) == 3.0
        assert subject.get_date(0) == '1.2.33'

    """
    Test der add_grade Methode auf mehrere Noten.
    """
    def test_multi_grade_added_size(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.size == 3

    """
    Test der Inhalte bei mehreren zugefügten Noten.
    """
    def test_multi_grade(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        assert subject.get_value(0) == 3.0
        assert subject.get_value(1) == 5.0
        assert subject.get_value(2) == 4.0
        assert subject.get_date(0) == '1.2.33'
        assert subject.get_date(1) == '1.2.44'
        assert subject.get_date(2) == '1.2.55'

    """
    Test auf mehr als 4 zugefügte Notenwerte.
    """
    def test_max_grades(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        subject.add_grade(Grade(1.0, '1.2.44'))
        subject.add_grade(Grade(2.0, '1.2.55'))
        assert subject.size == 4

    """
    Test des Mittelwertes bei fehlendem Noteneintrag.
    """
    def test_average_without_grade(self, subject):
        assert subject.get_average() == 0

    """
    Test des Mittelwertes bei einer Note.
    """
    def test_single_grade_average(self, subject):
        subject.add_grade(Grade(3.0, '1.2.33'))
        assert subject.get_average() == 3.0

    """
    Test des Mittelwertes bei mehreren zugefügten Noten.
    """
    def test_average(self, subject):
        subject.add_grade(Grade(2.0, '1.2.33'))
        subject.add_grade(Grade(5.0, '1.2.44'))
        subject.add_grade(Grade(4.0, '1.2.55'))
        subject.add_grade(Grade(1.0, '1.2.44'))
        assert subject.get_average() == 3.0


