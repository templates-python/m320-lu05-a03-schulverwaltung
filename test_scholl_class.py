import pytest
from school_class import SchoolClass
from classreport import ClassReport
from subject import Subject
from grade import Grade
from student import Student

class TestSchoolClass:

    @pytest.fixture
    def a_class(self):
        return SchoolClass('Musterklasse 23 A')

    @pytest.fixture
    def a_report(self):
        return ClassReport()

    def test_school_class_init(self, a_class):
        """
        Test der Initialisierung der Klasse
        """
        assert a_class.designation == 'Musterklasse 23 A'
        assert a_class.size == 0

    def test_single_student_added(self, a_class, a_report):
        max = Student("Max", a_report)
        a_class.add_student(max)
        assert a_class.take_student(0) is max

    def test_multi_student_added(self, a_class, a_report):
        for idx in range(4):
            a_class.add_student(Student('A', a_report))
        assert a_class.size == 4


    def test_max_student_added(self, a_class, a_report):
        for idx in range(22):
            a_class.add_student(Student('A', a_report))
        assert a_class.size == 20

    def test_student_list(self, a_class, a_report, capsys):
        a_class.add_student(Student('Max', a_report))
        a_class.add_student(Student('Mia', a_report))
        a_class.add_student(Student('Cem', a_report))
        a_class.add_student(Student('Ali', a_report))
        a_class.print_student_list()
        captured = capsys.readouterr()
        assert captured.out == 'Max\nMia\nCem\nAli\n'