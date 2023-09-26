from grade import Grade
from subject import Subject


class ClassReport:
    """
    Die Klasse stellt das Zeugnis einer Studentin dar.
    Im Zeugnis werden 3 Fächer aufgeführt (und genau 3 Fächer). Das lässt sich aus dem
    Klassendiagramm ableiten.

    Als Schnittstelle bietet die Klasse die Methoden
    - set_student(...)           setzt die Referenz auf ein Student-Objekt
    - add_subject(...)           setzt die Referenz auf ein Subject-Objekt
    - take_subject(i)             liefert das i-te Subject-Objekt
    - to_string()                liefert ein Zeugnis als String-Repräsentation
    - print_details()            git zu einem Fach alle Notenwerte mit Datum und den Schnitt aus

    Über die Methode to_string() kann das Zeugnis in einer Stingrepräsentation abgerufen werden.
    Sie umfasst den Namen des Studenten (Student) sowie die 3 Fächer mit dem Notenschnitt

    Die Methode print_details() gibt zu einem Fach alle Noten mit deren Datum sowie den Mittelwert aus.
    Als Parameter wird der Name des Fachs geliefert. Anhand dieses Namens wird dann in der Liste das
    korrekte Objekt ausfindig gemacht.

    Attribute:
    - subjects[]: die Referenz zu den 3 Fächer
    - student: die Referenz zum Student-Objekt

    """

    def __init__(self):
        """
        Erstellt ein Zeugnis mit einer leeren Fächerliste.
        """
        self._subjects = []
        self._student = None  # unbedingt auf None setzen, damit ein Wert gesetzt ist.
        # Siehe dazu den Code in der Methode to_string!

    # und hier die oben beschriebenen Methoden gemäss Klassendiagramm einfügen
    @property
    def size(self):  # findet sich nicht im Klassendiagramm, macht aber Sinn
        """
        Liefert die Anzahl der Fächer
        :return: Anzahl Fächer
        """
        return len(self._subjects)

    @property
    def student(self):
        """
        Liefert die Referenz des zugewiesenen Student-Objekts
        """
        return self._student

    @student.setter
    def student(self, student):
        """
        Setzt die Referenz zum Studenten
        :param student: Referenz zu Student
        """
        self._student = student

    def take_subject(self, index):
        """
        Liefert das durch index markierte Fach
        :param index: Nummer des Fachs
        :return: Referenz zu Fach
        """
        if index < self.size:
            return self._subjects[index]
        else:
            return None

    def add_subject(self, subject):
        """
        Setzt ein Fach
        :param subject: Referenz zum Fach
        """
        if self.size < 3:
            self._subjects.append(subject)

    def to_string(self):
        """
        Liefert eine String-Repräsentation des Zeugnises mit
        - Namen des Studenten
        - den Fächern
        - und dem jeweiligen Notenschnitt
        :return: Notenblatt als Stringrepräsentation
        """
        view = 'Zeugnis für: '
        if self._student is not None:
            # Nur wenn eine Referenz zu einem Studenten-Objekt existiert,
            # kann der Name abgefragt werden.
            view += self._student.name
        # alle Fächer mit dem Notenschnitt auflisten
        for subject in self._subjects:
            view += f'\n\t  {subject.name}:  {subject.average}'
        return view

    def print_details(self):
        """
        gibt alle Noten und den Schnitt der Fächer am Stdout aus.
        """
        for subject in self._subjects:
            # DEBUG
            print(f'\tFach: {subject.name} mit {subject.size} Noten')
            # DEBUG
            for count in range(subject.size):
                print(f'\t\t{count + 1} : {subject.take_value(count)} {subject.take_date(count)}')
            print(f'\tSchnitt: {subject.average}\n')


if __name__ == '__main__':
    # Zeugnis erzeugen...
    report = ClassReport()
    # ...und 3 Fächer zufügen.
    report.add_subject(Subject('Mathe'))
    report.add_subject(Subject('Deutsch'))
    report.add_subject(Subject('Turnen'))
    #
    # Jedem Fach noch Noten geben
    report.take_subject(0).add_grade(Grade(4.0, '1.1.11'))
    report.take_subject(0).add_grade(Grade(4.5, '2.2.22'))
    report.take_subject(1).add_grade(Grade(4.0, '3.3.33'))
    report.take_subject(1).add_grade(Grade(6.0, '4.4.44'))
    report.take_subject(1).add_grade(Grade(5.0, '5.5.55'))
    report.take_subject(2).add_grade(Grade(4.5, '6.6.66'))
    report.take_subject(2).add_grade(Grade(5.0, '7.7.77'))
    report.take_subject(2).add_grade(Grade(5.0, '8.8.88'))
    report.take_subject(2).add_grade(Grade(5.5, '9.9.99'))
    #
    # Alles im Detail ausgeben
    print(report.take_subject(0).name)
    report.print_details()
    #
    print(report.to_string())
