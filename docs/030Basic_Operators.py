"""
In diesem Abschnitt thematisieren wir grundlegende Operanden in Python.
Die +, -, *, / und % (modulo) Operanden auf Zahlen verhalten sich wie in Java. Es gilt ebenfalls Punkt vor Strich etc.
Es gibt zusätzlich den ** Operanden, welcher für das Potenzieren benutzt werden kann:
"""

######################################################################

print(1 + 2 * 3 / 4)  # Output: 2.5
print(10 % 3)  # Output: 1


num1 = 3 ** 2  # = 3 * 3 = 9
num2 = 2 ** 8  # = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 2^8 = 256
print(num1)  # 9
print(num2)  # 256

######################################################################

"""
Python unterstützt auch das Multiplizieren von Zeichenfolgen, um eine Zeichenfolge mit einer sich wiederholenden Sequenz zu bilden:
"""

######################################################################

string1 = "bla" * 4
print(string1)  # Output: blablablaba

######################################################################

"""
Dasselbe Prinzip funktioniert auch bei Listen :
"""

######################################################################

my_list = [0, 100, 5000] * 3
print(my_list)  # Output: [0, 100, 5000, 0, 100, 5000, 0, 100, 5000]

######################################################################


"""
Mit dem + Operator können Listen vereinigt werden. Hierbei werden alle Elemente der zweiten Liste am Ende der ersten Liste hinzugefügt.
"""

######################################################################

numbers = [0, 1, 2, 3]
large_numbers = [1001, 2000]
colors = ["red", "blue", "yellow"]

big_list = numbers + large_numbers + colors

# Output: [0, 1, 2, 3, 1001, 2000, 'red', 'blue', 'yellow']
print(big_list)

######################################################################

"""
Hier findest du eine Liste mit vielen Pthon Operatoren: https://www.w3schools.com/python/python_operators.asp
"""
