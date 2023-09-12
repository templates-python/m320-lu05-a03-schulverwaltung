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

    def __init__(self, designation):
        """
        Erzeugt eine Klasse mit deren Bezeichnung und stellt eine leere Liste
        für die Lernenden bereit.
        :param designation: Klassenbezeichnung
        """
        self._designation = designation
        self._students = []

    @property
    def designation(self):
        """
        Liefert die Klassenbezeichnung
        :return: Klassenbezeichnung
        """
        return self._designation


    def get_student(self, index):
        """
        Liefert das durch index markierte Element aus der Liste.
        :param index: Element-Nummer in der Liste
        :return: Elemente an der Stelle index
        """
        return self._students[index]

    def add_student(self, student):
        """
        Weist der Klasse einen Studenten zu. Die Klasse meldet sich dann umgehend beim Studenten
        mit der eigenen Referenz.
        Eine Klasse darf max. 20 Studierende haben.
        :param student: Studenten-Objekt
        :return:
        """
        if self.size < 20:
            self._students.append(student)
        else:
            print("Warnung: Student kann nicht zugefügt werden, da die Klasse voll ist")  # natürlich eine Exception

    @property
    def size(self):
        """
        Liefert die Anzahl Elemente in der Liste der Studenten
        :return: Anzahl Elemente
        """
        return len(self._students)

    def print_student_list(self):
        """
        Gibt eine Namensliste der Studenten aus
        """
        for student in self._students:
            print(student.name)

    def print_student_report(self, name):
        """
        Gibt das Zeugnis einer Studentin aus.
        Das korrekte Objekt wird anhand des Namens bestimmt.
        Bei einem falschen Namen erfolgt keine Ausgabe.
        :param name: Name des Studenten
        :return:
        """
        print("----")
        for student in self._students:
            if student.name == name:
                student.print_report()
                break


