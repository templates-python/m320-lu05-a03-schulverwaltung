from classreport import ClassReport
from grade import Grade
from student import Student
from subject import Subject


class SchoolClass:
    """
    Beschreibt eine Schulklasse mit der Klassenbezeichnung.
    Die Lernenden werden in einer Liste von Student-Objekten gehalten.

    Als Schnittstelle bietet die Klasse die Methoden
    - get_designation()            liefert den Namen der Klasse
    - add_student(...)             setzt die Referenz zu einem Student-Objekt
    - get_student(i)               liefert das i-te Student-Objekt aus der Liste
    - get_size()                   liefert die Anzahl der Student-Objekte in der Liste
    - print_student_list()         gibt die Namen aller Studenten aus
    - print_student_report(name)   gibt das Zeugnis für die Studentin / den Studenten mit name aus.

    Es ist bei der Implementation auf die Zusicherung der Klassengrösse zu achten.

    Attribute:
    - designation: Name der Klasse
    - students[]: Liste aller Student-Objekte
    """

    # DO IT