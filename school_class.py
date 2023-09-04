from student import Student
from class_report import ClassReport
from subject import Subject
from grade1 import Grade


class SchoolClass:
    '''
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

    Author:  René Probst
    Version: 1.0
    Date:    14.9.2022
    Changes: none
    '''

    def __init__(self, designation):
        '''
        Erzeugt eine Klasse mit deren Bezeichnung und stellt eine leere Liste
        für die Lernenden bereit.
        :param designation: Klassenbezeichnung
        '''
        self.__designation = designation
        self.__students    = []

    @property
    def designation(self):
        '''
        Liefert die Klassenbezeichnung
        :return: Klassenbezeichnung
        '''
        return self.__designation

    @property
    def student(self, index):
        '''
        Liefert das durch index markierte Element aus der Liste.
        :param index: Element-Nummer in der Liste
        :return: Elemente an der Stelle index
        '''
        return self.__students[index]

    def add_student(self, student):
        '''
        Weist der Klasse einen Studenten zu. Die lasse meldet sich dann umgehend beim Studneten
        mit der eigenen Referenz.
        Eine Klasse darf max. 20 Studierende haben.
        :param student: Studenten-Objekt
        :return:
        '''
        if self.size < 20:
            self.__students.append(student)
            print(student)
            #student.school_class(self)
        else:
            print("Warnung: Student kann nicht zugefügt werden, da die Klasse voll ist")  # natürlich eine Exception


    @property
    def size(self):
        '''
        Liefert die Anzahl Elemente in der Liste der Studenten
        :return: Anzahl Elemente
        '''
        return len(self.__students)

    def print_student_list(self):
        '''
        Gibt eine Namensliste der Studenten aus
        '''
        for student in self.__students:
            print(student.name)


    def print_student_report(self, name):
        '''
        Gibt das Zeugnis einer Studentin aus.
        Das korrekte Objekt wird anhand des Namens bestimmt.
        Bei einem falschen Namen erfolgt keine Ausgabe.
        :param name: Name des Studenten
        :return:
        '''
        print("----")
        for student in self.__students:
            if student.name == name:
                student.print_report()
                break


if __name__ == "__main__":
    # Am Anfang steht da eine Klasse
    the_class = SchoolClass("IM993a")
    #
    # Dann braucht es mal ein paar leere Zeugnisse und deren Fächer
    report_max = ClassReport()
    report_max.add_subject(Subject("Mathe"))
    report_max.add_subject(Subject("Deutsch"))
    report_max.add_subject(Subject("Turnen"))
    #
    report_pia = ClassReport()
    report_pia.add_subject(Subject("Mathe"))
    report_pia.add_subject(Subject("Deutsch"))
    report_pia.add_subject(Subject("Turnen"))
    #
    # Und natürlich Lernende
    max = Student("Max", report_max)
    pia = Student("Pia", report_pia)
    #
    # Nun immatrikulieren wir die Lernenden
    the_class.add_student(max)
    the_class.add_student(pia)
    # Und dann erstellen wir mal die Klasseliste
    the_class.print_student_list()
    #
    # Jetzt braucht es noch Noten
    report_max.get_subject(0).add_grade(Grade(4.0, "1.1.11"))
    report_max.get_subject(0).add_grade(Grade(4.5, "2.2.22"))
    report_max.get_subject(1).add_grade(Grade(4.0, "3.3.33"))
    report_max.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
    report_max.get_subject(1).add_grade(Grade(5.0, "5.5.55"))
    report_max.get_subject(2).add_grade(Grade(4.5, "6.6.66"))
    report_max.get_subject(2).add_grade(Grade(5.0, "7.7.77"))
    report_max.get_subject(2).add_grade(Grade(5.0, "8.8.88"))
    report_max.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
    #
    report_pia.get_subject(0).add_grade(Grade(5.5, "1.1.11"))
    report_pia.get_subject(0).add_grade(Grade(5.5, "2.2.22"))
    report_pia.get_subject(1).add_grade(Grade(4.5, "3.3.33"))
    report_pia.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
    report_pia.get_subject(1).add_grade(Grade(5.5, "5.5.55"))
    report_pia.get_subject(2).add_grade(Grade(4.0, "6.6.66"))
    report_pia.get_subject(2).add_grade(Grade(5.5, "7.7.77"))
    report_pia.get_subject(2).add_grade(Grade(6.0, "8.8.88"))
    report_pia.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
    #
    the_class.print_student_report("Max")
    the_class.print_student_report("Pia")
    the_class.print_student_report("Theo")
