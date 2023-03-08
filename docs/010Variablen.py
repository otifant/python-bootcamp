"""
In Python werden variablen initialisiert, sobald sie einen Wert zugewiesen bekommen.
Es benötigt weder die Verwendung eines Keywords (wie z.B. new), Noch die Angabe eines Datentypen.
Dies ist nämlich nicht erforderlich, da alle variablen als Objekte angesehen werden. Python bestimmt im Hintergrund, um welchen Datentyp es sich hierbei handelt. 

Das Einfachste Beispiel lautet ganz einfach x = 5

In Python ist es üblich ein sogenanntes Snake Case naming zu wählen, nicht wie in Java Camel oder Pascal Case.
Dabei werden Wörter einfach mit einem Unterstrich (also "_") getrennt. 
Variablennamen starten wie üblich mit einem Kleinbuchstaben, Klassen mit einem Grossbuchstaben.

Einige Beispiele für die Initialisierung und Operationen mit Variablen: 
"""

######################################################################

my_int = 7
print(my_int)  # Output: 7

my_float = 7.0
print(my_float)  # Output: 7.0

my_float = float(my_int)  # Typ-casting von int zu float
print(my_float)  # Output: 7.0

my_string1 = 'Hello'  # Initialisierung eines Strings mit '
my_string2 = "Hello"  # Initialisierung eines Strings mit "

# Initialisierung mit ", der Apostroph wird hier als character angesehen.
my_string3 = "Don't worry about apostrophes"
# Initialisierung mit ', Anführuns- und Schlusszeichen werden hier als character angesehen.
my_string4 = 'I just want to say "Hello"'

my_int2 = 1
my_int3 = 2
my_int4 = my_int2 + my_int3
print(my_int4)  # Output: 3


hello = "hello"
world = "world"
hello_world = hello + " " + world
print(hello_world)  # Output: hello world


######################################################################

"""
Aber Vorsicht! Zahlen können nicht mit Strings addiert werden! Folgender Code wirft einen Error:
"""

######################################################################

# This will not work!
my_number = 1
my_string = "hello"

# print(my_string + my_number)  # TypeError

######################################################################

"""
Der Fehler wird hier zu Laufzeit des Programms geworfen, der Compiler bemerkt den Fehler nämlich nicht.
Die Lösung des Problems sind sogenannte formatted Strings oder einfach f-Strings. Eine Möglichkeit ist die folgende:
"""

######################################################################

my_number = 1
my_string = "hello"

print(f'my_number is {my_number} and my_string is "{my_string}"')
#Output: my_number is 1 and my_string is "hello"

######################################################################

"""
Ein weiteres cooles Feature in Python ist die Mehrfachzuweisung. Folgende Beispiele sind valider Python code:
"""

######################################################################

x, y, z = 10, 41, 5.0
a = b = c = "Hello"

######################################################################


"""
Hier wurde x der Wert 10, y der Wert 41 und z den Wert 5.0 zugewiesen.
In der zweiten Zeile wurde den Variablen a, b und c jeweils der String "Hello" zugewiesen.
"""


"""
Zusatz: Casting

Wie auch in anderen Programmiersprachen können Datentypen gecastet werden.
Folgend einige Beispiele, das Prinzip sollte klar sein:
"""

######################################################################

a = str(100)  # a = '100'
b = int(4.2)  # b = 4
c = float(7)  # c = 7.0
d = int('42')  # d = 42

######################################################################


