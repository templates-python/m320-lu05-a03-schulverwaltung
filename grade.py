from dataclasses import dataclass


@dataclass
class Grade:
    """
    Die Klasse Grade beschreibt eine Note mit einem Wert (value) und dem Datum (date) an dem die
    Note realisiert wurde.
    Das Objekt wird bei der Erzeugung mit den entsprechenden Werten initialisiert und kann dann nur
    gelesen werden.

    Attribute:
    - value: ein Notenwert von 1...6 (der Wert muss in der Zuweisung gesichert werden)
    - date:  eine Zeichenkette, die ungeprüft das Datum der Note repräsentiert.

    Author:  René Probst
    Version: 1.0
    Date:    14.9.2022
    Changes: none
    """

    value: float = -1.0
    date: str = '1.1.1111'

    def __init__(self, value, date):
        """
        Erstellt ein Notenobjekt mit dem Notenwert und dem Datum der Notengebung
        :param value: Notenwert der Prüfung
        :param date:  Datum der Prüfung
        """
        if 1.0 <= value <= 6.0:
            self._value = value
        else:
            self._value = -1.0  # ungültiger Notenwert (ja, hier würde man eine Exception werfen)
        self._date = date  # und da wird einfach alles entgegengenommen



    @property
    def value(self):
        return self._value

    @property
    def date(self):
        return self._date




# Test der Klasse mit eigener main-Methode
if __name__ == '__main__':
    # ein Notenobjekt erzeugen mit korrekten Notenwert
    grade = Grade(4.0, '3.2.22')
    print(f'Notenwert:  {grade.value}')
    print(f'Datum:      {grade.date}')
    # ein Notenobjekt erzeugen mit ungültigem Notenwert --> -1 wird angezeigt
    grade = Grade(6.5, '1.1.99')
    print(f'\nNotenwert: {grade.value}')
    print(f'Datum:       {grade.date}')
