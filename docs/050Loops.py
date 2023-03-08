"""
For-Loop

Es gibt mehrere Möglichkeiten, einen For-Loop in Python zu implementieren. 
Eine Möglichkeit ist die Benutzung der range() methode, welche wiederum selbst verschieden eingesetzt werden kann. 
Eine andere Möglichkeit ist einfach über alle Elemente einer Liste (oder auch eines Sets, Dictionarys, ...) zu iterieren.
Beachte den Doppelpunkt und die Einrückung des Bodys.
Das Nachfolgende Beispiel sollte Klarheit verschaffen.
"""

######################################################################

for i in range(10):  # i = 0, 1, 2, ... , 9
    print(i)

for i in range(3, 8):  # i = 3, 4, 5, 6, 7
    print(i)

for i in range(2, 9, 3):  # i = 2, 5, 8
    print(i)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:  # prints out every number in the numbers list
    print(number)

######################################################################

"""
While-Loop

Der While Loop funktioniert genau wie in Java auch. Hier ein Beispiel:

"""

######################################################################

i = 0
while i < 5:
    print(i)
    i += 1

######################################################################

"""
Die Statements "break" and "continue" sollten bekannt sein und funktionieren ebenfalls wie in Java.
"""


# https://www.learnpython.org/en/Loops
# Can we use "else" clause for loops?
