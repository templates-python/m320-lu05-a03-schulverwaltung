from dataclasses import dataclass


@dataclass
class Grade:
    """
    Die Klasse Grade beschreibt eine Note mit einem Wert (value) und dem Datum (date) an dem die
    Note realisiert wurde.
    Das Objekt wird bei der Erzeugung mit den entsprechenden Werten initialisiert und kann dann nur
    gelesen werden.

    Attribute:
    - value: ein Notenwert von 1 ... 6 (der Wert muss in der Zuweisung gesichert werden)
    - date:  eine Zeichenkette, die ungeprüft das Datum der Note repräsentiert.

    Author:
    Version: 1.0
    Date:
    Changes: none
    """

    # DO IT