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

    # DO IT
