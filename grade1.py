class Grade1:
    '''
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
    '''

    def __init__(self, value, date):
        '''
        Erstellt ein Notenobjekt mit dem Notenwert und dem Datum der Notengebung
        :param value: Notenwert der Prüfung
        :param date:  Datum der Prüfung
        '''
        if value >= 1.0 and value <= 6.0:
            self.__value = value
        else:
            self.__value = -1.0 # ungültiger Notenwert (ja, hier würde man eine Exception werfen)
        self.__date  = date     # und da wird einfach alles entgegengenommen

    @property
    def value(self):
        '''
        Liefert den Notenwert
        :return: Notenwert
        '''
        return self.__value

    @property
    def date(self):
        '''
        Liefert das Datum der Notenerhebung
        :return: Datum
        '''
        return self.__date
    print('init done')


# Test der Klasse mit eigener main-Methode
if __name__ == '__main__':
    # ein Notenobjekt erzeugen mit korrekten Notenwert
    grade = Grade1(4.0, '3.2.22')
    print(f'Notenwert:  {grade.value}')
    print(f'Datum:      {grade.date}')
    # ein Notenobjekt erzeugen mit ungültigem Notenwert --> -1 wird angezeigt
    grade = Grade1(6.5, '1.1.99')
    print(f'\nNotenwert: {grade.value}')
    print(f'Datum:       {grade.date}')
