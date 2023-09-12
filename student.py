from classreport import ClassReport
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
    """

    # DO IT