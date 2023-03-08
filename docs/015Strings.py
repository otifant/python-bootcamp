"""
Strings können in Python mit einfachen oder doppelten Anführungszeichen initialisiert werden.
Ebenfalls ist es möglich, Strings über mehrere Zeilen mit dreifach doppelten oder dreifach einfachen Anführungszeichen zu initialisieren.
Hierbei werden die Leer- und Enterzeichen mitgespeichert. Ein String über 3 Zeilen wird bei einem print() Aufruf auch über 3 Zeilen in der Konsole ausgegeben.
Im nachfolgenden Code findest du ein paar Beispiele:
"""
######################################################################

random_string = "Hello"
random_string2 = 'World'

random_multiline_string = """Say
my
name!"""

random_multiline_string2 = '''Hello
my name is
Jeff'''

print(random_multiline_string2)
# Output:
# Hello
# my name is
# Jeff

######################################################################

"""
Strings sind wie Arrays! Man kann auf die Elemente (Character; Buchstaben) mit dem [] Operator zugreifen.
Ebenfalls kann man mit Loops über Strings iterieren oder die die Länge des Strings ausgeben lassen.
Welche Loops es gibt und wie man sie implementiert wird in einem späteren Kappitel behandelt.
Einige Operationen mit Strings sind im nachfolgenden Code zu finden:
"""

######################################################################

a = "Hello World!"
print(len(a))  # 12
print(a[1])  # e

# Jedes Zeichen wird auf einer separaten Zeile ausgegeben:
for x in a:
    print(x)

print("orl" in a)  # True
print("i" not in a)  # True
######################################################################

"""
Eine weitere coole Operation auf Strings ist das sogenannte "Slicin". 
Wie der Name schon suggeriert, kann man Strings in verschiedene Teile zerlegen. Dabei nehmen wir aber nicht einzelne Buchstaben wie vorher,
sondern ganze Teile. Einige slicing Operationen sind:
"""

######################################################################

beispiel = "Python ist eine tolle Programmiersprache!"

# Herausschneiden zwischen dem ersten und zweiten Index.
# Beachte, dass der Buchstabe mit dem 2. Index nicht inklusive ist.
print(beispiel[2:12])  # thon ist ei
print(beispiel[2:4])  # th

# Herausschneiden der ersten Buchstaben
print(beispiel[:5])  # Pytho
print(beispiel[:20])  # Python ist eine toll

# Weglassen der ersten Buchstaben
print(beispiel[4:])  # on ist eine tolle Programmiersprache!
print(beispiel[22:])  # Programmiersprache!

# Start beim 8. letzten Buchstaben, Ende beim 5. letzten Buchstaben.
print(beispiel[-8:-5])  # spr
print(beispiel[-19:-10])  # Programmi

######################################################################

"""
Wie auch in Java hat Python einige vordefinierte Methoden auf Strings. Einige sind nachfolgend Aufgelistet:
Falls du noch weitere Methoden sehen möchtest gibt es hier eine grosse Liste: https://www.w3schools.com/python/python_strings_methods.asp
"""

######################################################################

s = "Python is fun!"

print(s.upper())  # PYTHON IS FUN!
print(s.lower())  # python is fun!

# Ersetzen eines Substrings mit einem anderen Substring
print(s.replace("n", "m"))  # Pythom is fum!
print(s.replace(" ", "#"))  # Python#is#fun!
print(s.replace("Python", "Java"))  # Java is fun!

# .strip() entfernt alle Leerzeichen am Anfang und am Ende
print("     to many whitespaces     ".strip())  # to many whitespaces

# .split() gibt eine Liste mit substrings zurück.
print(s.split(" "))  # ['Python', 'is', 'fun!']
print(s.split("n"))  # ['Pytho', ' is fu', '!']
print(s.split("is"))  # ['Python ', ' fun!']

# Strings können mit dem + Operator aneinandergeheftet werden.
print(s + " Java too!")  # Python is fun! Java too!

######################################################################

"""
Escape Character

Um Zeichen in einem String hinzufügen zu können, welche normalerweise nicht erlaubt sind, kann ein \ verwendet werden.
Es gibt auch weitere spezielle Zeichen, welche mit Hilfe eines Backslashes in einen String eingefügt werden können.
"""

######################################################################

# ' muss nicht escaped werden, " aber schon.
print("Es gibt einfache (') und doppelte (\") Anführungszeichen")
# Hier ist es genau umgekehrt
print('Es gibt einfache (\') und doppelte (") Anführungszeichen')
# Escapen des Escape characters
print("Ich verwende ein \\, um zu escapen")

######################################################################

"""
\n      newline
\t      tab
"""
