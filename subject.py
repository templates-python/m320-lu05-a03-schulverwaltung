from grade import Grade


class Subject:
    """
    Die Klasse repräsentiert ein Schulfach (school subject) mit 2 bis 4 Noten.
    Die Noten-Objekte (Grade) werden in einer Liste abgelegt. Über einen Index kann
    auf das i-te Objekt zugegriffen werden.
    Als Schnittstelle bietet die Klasse die Methoden
    - get_name()       Name des Fachs
    - add_grade(..)    Fügt ein Note-Objekt dem Fach zu (max. 4 Noten)
    - get_size()       Anzahl der gespeicherten Noten-Objekte
    - get_value(i)     Notenwert der i-ten Note
    - get_date(i)      Datum der i-ten Note
    - get_average()    Mittelwert aus den i Noten

    Attribute:
    - name: Name des Fachs
    - grades[]: eine Liste mit 2 bis 4 Noten-Objekten
    """

    def __init__(self, name):
        """
        Erzeugt ein Fach mit der Fachbezeichnung (name) und eine leere Liste für die Noten.
        Es könne max. 4 Noten zugewiesen werden.
        :param name: Name des Fachs
        """
        self._name = name
        self._grades = []

    # und hier die oben beschriebenen Methoden gemäss Klassendiagramm einfügen
    @property
    def name(self):
        """
        Liefert den Namen des Fachs
        :return: Name des Fachs
        """
        return self._name

    def add_grade(self, grade):
        """
        Fügt ein Noten-Objekt der Liste zu.
        Es wird sichergestellt, dass max. 4 Noten eingefügt sind.
        :param grade: Noten-Objekt
        """
        if self.size < 4:
            self._grades.append(grade)
        # Und sonst passiert nichts. Das Notenobjekt wandert ins Nirvana

    @property
    def size(self):
        """
        Liefert die Anzahl der Noten-Objekte in der Liste
        :return: Anzahl  Objekte
        """
        return len(self._grades)

    def take_value(self, index):
        """
        Liefert den Notenwert des i-ten Objekts.
        :param index: Index der Liste
        :return: Notenwert des durch index markierten Objekts oder 0 bei falschem Index
        """
        if index < self.size:
            grade = self._grades[index]
            return grade.value
        else:
            return 0  # Fehlercode (auch hier wird in einer Applikation dann eine Exception erzeugt)

    def take_date(self, index):
        """
        Liefert das Datum des i-ten Objekts.
        :param index: Indes der Liste
        :return: datum des durch index markierten Objekts oder nichts bei falschem Index
        """
        if index < self.size:
            grade = self._grades[index]
            return grade.date


    @property
    def average(self):
        """
        Liefert den Notenschnitt des Fachs
        Gemäss Klassendiagramm müssen 2..4 Notenwerte vorliegen. Hier müsste daher eine
        Prüfung auf die Anzahl Noten gegeben sein (if self.size >= 2) und bei nicht erfüllen eine
        entsprechende Exception geworfen werden. Aber das lassen wir hier bleiben.
        :return: Notenschnitt
        """
        if self.size == 0:
            return 0
        else:
            sum = 0.0
            for number in range(self.size):
                sum += self.take_value(number)
            return sum / self.size


# Klasse testen mit main
if __name__ == '__main__':
    sub = Subject('Mathe')
    sub.add_grade(Grade(4.0, '1.1.11'))
    sub.add_grade(Grade(5.0, '2.2.22'))
    sub.add_grade(Grade(5.0, '3.3.33'))
    print(f'{sub.name} {sub.average} - Mittelwert aus {sub.size} Werten')
    sub.add_grade(Grade(6.0, '4.4.44'))
    sub.add_grade(Grade(5.5, '5.5.55'))
    print(f'{sub.name} {sub.average} - Mittelwert aus {sub.size} Werten')
