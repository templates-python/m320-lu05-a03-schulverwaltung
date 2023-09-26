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
    - take_value(i)     Notenwert der i-ten Note
    - take_date(i)      Datum der i-ten Note
    - get_average()    Mittelwert aus den i Noten

    Attribute:
    - name: Name des Fachs
    - grades[]: eine Liste mit 2 bis 4 Noten-Objekten
    """

    # DO IT
