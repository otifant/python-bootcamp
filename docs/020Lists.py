"""
In Python gibt es keine Arrays, dafür Listen. 
Eine Liste (engl "List") ist im Prinzip ein Array, benutzt auch die gleiche Syntax wie ein Array in Java, hat aber die Funktionalitäten einer ArrayList.
Wir sehen im folgenden Code-Beispiel wie mit Listen gearbeitet werden kann. 
Da in Python alle Variablen als Objekte gespeichert sind, kann man in eine Liste auch verschiedene Datentypen einfügen.
Aber Vorsicht! Dies ist nicht zu empfehlen und Fehleranfällig!
Einige Funktionen, wie zum Beispiel das Sortieren funktioniert nicht bei einer Liste mit unterschiedlichen Datentypen!

"""

######################################################################
my_list = []  # create an empty list
my_list.append(1)  # add (int) 1 to the list
my_list.append(2)
my_list.append("Regenschirm")  # add (str) "Regenschirm" to the list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2
print(my_list[2])  # Output: Regenschirm

my_list2 = [1, 2, "Regenschirm"]  # initialize the same list directly
my_list2.pop(0)  # Remove element at pos 0

print(my_list2)  # Output: [2, 'Regenschirm']

######################################################################

"""
In diesem Beispiel sieht man, dass das Printen einer Liste einfach mit print(list) machbar ist. Es braucht hierfür keine toString Methode wie z.B. in Java.
Hilfreiche Operationen bezüglich Listen sind die folgenden:
"""

######################################################################

list_name = []  # leere Liste initialisieren
list_name = {"element1", "element2"}  # Initialisierung mit Elementen
# Initialisierung mit Elementen via Konstruktor
list_name = list(("element1", "element2"))

list_name.append("element")  # fügt ein Element am Ende hinzu
# fügt das Element an der angegebenen Position hinzu
list_name.insert("position", "element")

list_name.pop("position")  # löscht das Element an der angegebenen Position
list_name.remove("element")  # löscht das angegebene Element
list_name.clear()  # löscht alle Elemente

len(list_name)  # gibt die Länge (anzahl Elemente) zurück
list_name.reverse()  # dreht die Reihenfolge der Liste um
list_name.sort()  # sortiert die Liste

# gibt den Index des ersten elementes mit diesem Wert aus
list_name.index("element")
######################################################################


"""
Zusatz: 
Wir haben zuvor die Mehrfachzuweisung von Variablen kennengelernt. 
Diese können wir nun anwenden, um Werte direkt aus einer Liste zu extrahieren und in Variablen zu speichern.
Siehe folgendes Beispiel:
"""

######################################################################

numbers = [31, 5007, 19]
x, y, z = numbers
print(x)  # 31
print(y)  # 5007
print(z)  # 19

######################################################################
