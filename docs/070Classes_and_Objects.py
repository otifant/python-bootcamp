"""
Der allgemeine Aufbau und Verwendungszweck von Klassen sollte aus dem Java Ausbildungsprogramm bekannt sein.
Klassen sind in Python dynamischer Natur, sie werden zu Laufzeit des Programms konstruiert und können mödifiziert werden.
Es können also dynamisch Attribute (Member-Variablen) der Klasse hinzugefügt werden.
Man muss sich auch bewusst sein, dass aufgrund dieser Möglichkeit Bugs entstehen können.
Vertippt sich ein Programmierer, so wird das Programm eine bestehende Membervariable nicht überschreiben, sondern einfach eine neue hinzufügen!

Wichtig zu erwähnen ist zusätzlich, dass bei einer Memberfunktion (welche nicht statisch ist) der Parameter self übergeben werden muss.
Das Keyword "self" ist analog zu Verstehen wie "this" in Java.
Der Konstruktor der Klasse wird mit def __init__(self, arg1, arg2, ...): definiert.

Folgendes Beispiel sollte Klarheit verschaffen:
"""

######################################################################


class MyClass:
    """A simple Class for demonstration"""

    # Constructor
    def __init__(self, var2: int, var3: list[str]) -> None:
        self.member_var1 = "Hello"
        self.member_var2 = var2
        self.member_var3 = var3

    def print_variables(self) -> None:
        """prints out all member variables on a separate line"""
        print(f'member_var1: {self.member_var1}\n' +
              f'member_var2: {self.member_var2}\n' +
              f'member_var3: {self.member_var3}')


myObject = MyClass(3, ["Hello", "World", "!"])  # create instance
myObject.member_var1 = "Grüezi"  # change member_var1
myObject.member_var4 = 42.0  # add a 4th member variable
myObject.print_variables()  # call member function
print(myObject.member_var4)

######################################################################

"""
Instance Variables vs Class Variables

Wir haben im vorherigen Beispiel gesehen, wie man eine Klasse in Python initialisiert und Attribute hinzufügt.
Diese Attribute sind sogenannte "Instance Variables". Jedes erstellte Objekt der Klasse besitzt seine eigen "Werte"
Es gibt in Python auch sogenannte "Class Variables". Diese haben bei jedem Objekt der Klasse denselben Wert (vergleichbar mit einer statischen Variablen in Java)
Siehe folgendes Beispiel:
"""

######################################################################


class Car:
    color: str = "red"  # class variable

    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower


car1 = Car("audi", 230)
car2 = Car("suzuki", 110)

print(car1.color)  # red
print(car2.color)
car2.color = "blue"
print(car1.color)  # green
print(car2.color)


######################################################################


# https://docs.python.org/3/tutorial/classes.html

# @dataclass
