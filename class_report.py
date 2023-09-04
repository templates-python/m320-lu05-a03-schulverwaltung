from subject import Subject
from grade1 import Grade

class ClassReport:
    '''
    Die Klasse stellt das Zeugnis einer Studentin dar.
    Im Zeugnis werden 3 Fächer aufgeführt (und genau 3 Fächer). Das lässt sich aus dem
    Klassendiagramm ableiten.

    Als Schnittstelle bietet die Klasse die Methoden
    - set_student(...)           setzt die Referenz auf ein Student-Objekt
    - add_subject(...)           setzt die Referenz auf ein Subject-Objekt
    - get_subject(i)             liefert das i-te Subject-Objekt
    - to_string()                liefert ein Zeugnis als String-Repräsentation
    - print_details()            git zu einem Fach alle Notenwerte mit Datum und den Schnitt aus

    Über die Methode to_string() kann das Zeugnis in einer Stingrepräsentation abgerufen werden.
    Sie umfasst den Namen des Studenten (Student) sowie die 3 Fächer mit dem Notenschnitt

    Die Methode print_details() gibt zu einem Fach alle Noten mit deren Datum sowie den Mittwelwert aus.
    Als Parameter wird der Name des Fachs geliefert. Anhand dieses Namens wird dann in der Liste das
    korrekte Objekt ausfindig gemacht.

    Attribute:
    - subjects[]: die Referenz zu den 3 Fächer
    - student: die Referenz zum Student-Objekt

    Author:  René Probst
    Version: 1.0
    Date:    14.9.2022
    Changes: none
    '''

    def __init__(self):
        '''
        Erstellt ein Zeugnis mit einer leeren Fächerliste.
        '''
        self.__subjects = []
        self.__student = None # unbedingt auf None setzen, damit ein Wert gesetzt ist.
                              # Siehe dazu den Code in der Methode to_string!


    # und hier die oben beschriebenen Methoden gemäss Klassendiagramm einfügen
    @property
    def size(self):  # findet sich nicht im Klassendiagramm, macht aber Sinn
        '''
        Liefert die Anzahl der Fächer
        :return: Anzahl Fächer
        '''
        return len(self.__subjects)

    def set_student(self, student):
        '''
        Setzt die Referenz zum Studenten
        :param student: Referenz zu Student
        '''
        self.__student = student


    def get_subject(self, index):
        '''
        Liefert das durch index markierte Fach
        :param index: Nummer des Fachs
        :return: Referenz zu Fach
        '''
        return self.__subjects[index]


    def add_subject(self, subject):
        '''
        Setzt ein Fach
        :param subject: Referenz zum Fach
        '''
        if self.size < 3:
           self.__subjects.append(subject)


    def to_string(self):
        '''
        Liefert eine String-Repräsentation des Zeugnis mit
        - Namen des Studenten
        - den Fächern
        - und dem jeweiligen Notenschnitt
        :return: Notenblatt als Stringrepräsentation
        '''
        view = "Zeugnis für: "
        if self.__student != None:
            # Nur wenn eine Referenz zu einem Studenten-Objekt existiert,
            # kann der Name abgefragt werden.
            view += self.__student.name
        # alle Fächer mit dem Notenschnitt auflisten
        for subject in self.__subjects:
            view += "\n\t" + subject.name + ":  " + str(subject.get_average())
        return view

    def print_details(self):
        '''
        gibt alle Noten und den Schnitt der Fächer am Stdout aus.
        '''
        for subject in self.__subjects:
            #DEBUG
            print("\tFach: " + subject.name + " mit " + str(subject.size) + " Noten")
            #DEBUG
            for count  in range(subject.size):
               print("\t\t" + str(count+1) + ": " + str(subject.get_value(count)) + "   " + str(subject.get_date(count)) )
            print("\tSchnitt: " + str(subject.get_average()) + "\n")


if __name__ == "__main__":
    # Zeugnis erzeugen...
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
    # Alles im Detail ausgeben
    print(report.get_subject(0).name)
    report.print_details()
    #
    print(report.to_string())
