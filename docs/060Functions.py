"""
Kommen wir zum Thema Funktionen.
Eine Funktion in Python ist das, was wir in Java eine Methode nennen. Das Gundprinzip sollte klar sein.
Funktionen werden immer mit dem keyword "def" definiert. Bei einer Funktion des Typs void (ohne Rückgabewert) braucht es kein zusätzliches Keyword.
Eine Funktion ist in Python folgendermassen aufgebaut:
"""

######################################################################


def funktion_name(arg1, arg2):
    # body
    return  # can be omited

######################################################################


"""
Zwei Beispiele könnten die Folgenden sein:
"""

######################################################################


def print_hello():
    print("Hello")


def sum(i, j):
    return i + j


# Call the defined functions
print_hello()
print(sum(1, 6))


######################################################################

"""
Es können noch einige zusätziche Informationen bei der Definition angegeben werden, wie Beispielsweise
Ein Docstring (Beschreibung der Funktion), ein Return Datentyp und Datentypen der Parameter.
Die Funktionen von Oben könnten also wie folgt angepasst werden:
"""

######################################################################


def print_hello() -> None:
    """Prints 'Hello' to the console"""
    print("Hello")


def sum(i: int, j: int) -> int:
    """Returns the sum of i and j"""
    return i + j


######################################################################
"""
Dies ist aber nur eine Information und hat keinen Einfluss auf das Programm oder den Compiler!
Der Funktionaufruf sum(1, "green") würde ausgeführt und das Programm einen Fehler werfen!
Daher ist es von Vorteil, Docstrings sowie Paremeter und Rückgabetypen anzugeben, um während dem Code Schreiben mögliche Fehler besser zu erkennen.
Durch hovern über die Methode sind diese Informationen ersichtlich.

Eine Liste mit Datentypen in Python gibt es hier: https://www.w3schools.com/python/python_datatypes.asp
"""
