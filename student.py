from class_report import ClassReport
from grade import Grade
from subject import Subject


#
class Student:
    """
    Die Klasse beschreibt eine Studentin mit Name als alleiniges Merkmal.

    Als Schnittstelle bietet die Klasse die Methoden
    - get_name()            liefert den Namen der Studentin / des Studenten
    - get_school_class()    liefert die Referenz zum Klassen-Objekt
    - set_scholl_class(...) setzt die Referenz zum Klassen-Objekt
    - get_report()          liefert - über to_string() von ClassReport) - das Zeugnis
    - print_report()        gibt das Zeugnis aus

    Attribute:
    - name: Name des Studenten
    - the_class: Referenz zum Klassen-Objekt
    - report: Referenz zum Zeugnis

    Author:  René Probst
    Version: 1.0
    Date:    14.9.2022
    Changes: none
    """

    def __init__(self, name, report):
        """
        Erzeugt ein Student-Objekt mit Name und einer Referenz zum Zeugnis.
        :param report: Referenz zum Zeugnis
        """
        self.__name = name
        self.__report = report
        self.__school_class = None  # diese Referenz folgt zeitlich später
        # hier sofort die zweiseitige Beziehung knüpfen.
        report.set_student(self)

    # und hier die oben beschriebenen Methoden gemäss Klassendiagramm einfügen

    @property
    def name(self):
        """
        Liefert den Namen des Studenten
        :return: Name des Studenten
        """
        return self.__name

    @property
    def school_class(self):
        """
        Liefert die Referenz der Klasse
        :return: Referenz der Klasse
        """
        return self.__school_class

    @school_class.setter
    def school_class(self, school_class):
        """
        Setzt die Referenz zur Klasse
        :param school_class: Referenz der Klasse
        """
        self.__school_class = school_class

    @property
    def report(self):
        """
        Liefert die Referenz zum Zeugnis
        :return: Referenz zum Zeugnis
        """
        return self.__report

    def print_report(self):
        print(self.report.to_string())


if __name__ == "__main__":
    report = ClassReport()
    # ...und 3 Fächer zufügen.
    report.add_subject(Subject("Mathe"))
    report.add_subject(Subject("Deutsch"))
    report.add_subject(Subject("Turnen"))
    #
    # Jedem Fach noch Noten geben
    report.get_subject(0).add_grade(Grade(4.0, "1.1.11"))
    report.get_subject(0).add_grade(Grade(4.5, "2.2.22"))
    report.get_subject(1).add_grade(Grade(4.0, "3.3.33"))
    report.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
    report.get_subject(1).add_grade(Grade(5.0, "5.5.55"))
    report.get_subject(2).add_grade(Grade(4.5, "6.6.66"))
    report.get_subject(2).add_grade(Grade(5.0, "7.7.77"))
    report.get_subject(2).add_grade(Grade(5.0, "8.8.88"))
    report.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
    #
    student = Student("Orkan", report)
    student.print_report()
