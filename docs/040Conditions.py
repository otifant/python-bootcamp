"""
In Python gibt es natürlich auch bool'sche ausdrücke. Die meisten Operanden wie ==, <=, <, >, >=, != sollten bekannt sein und funktionieren gleich wie in Java.
Zusätzlich gibt es folgende Operatoren:

and         Funktioniert analog dem && Operator aus Java
or          Funktioniert analog dem || Operator aus Java
in          Gibt True zurück falls ein Element in einem Objekt (z.B. einer Liste) vorhanden ist, sonst False
is          Im Gegensatz zum „==“ vergleicht der is-Operator nicht die Werte der Variablen, sondern die Instanzen selbst. Siehe Beispiel unten.
not         Negiert einen bool'schen Ausdruck

Im Folenden Beispiele werden alle print statements ausgeführt, weil alle if-Bedinungen zu True evaluieren:
"""

######################################################################

a = True
b = False

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # Output: True
print(x is y)  # Output: False

if a and b == False:
    print("a is True and b is False.")

if a or b:
    print("Either a, b or both of them are True.")

if 1 in x:
    print("1 is in x.")

if not b:
    print("b is false.")


######################################################################

