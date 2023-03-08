"""
Dictionaries funktionieren ähnlich wie Arrays (bzw. Listen). Der Zugriff auf den Inhalt erfolgt aber mit Schlüsseln (sogenannte Keys) und nicht mit indexen.
Im Folgenden Beispiel wird ein Dictionary mit email-addressen von Personen erstellt.
"""

######################################################################

email_database = {}  # initialize empty dictionary

# add a new entry with key "John" and value "John.Guildmore@gmail.com"
email_database["John"] = "John.Guildmore@gmail.com"

email_database["Jack"] = "jack_reacher@hotmail.com"

print(email_database["John"])  # John.Guildmore@gmail.com
print(email_database)
# {'John': 'John.Guildmore@gmail.com', 'Jack': 'jack_reacher@hotmail.com'}


######################################################################

"""
Natürlich kann man dasselbe Dictionary auch direkt befüllt initialisieren:
"""

######################################################################

email_database = {
    "John": "John.Guildmore@gmail.com",
    "Jack": "jack_reacher@hotmail.com"
}

######################################################################

"""
Einige wichtige Operationen mit Dictionaries sind:
"""

######################################################################

dict_name = {}  # Leeres Dictionary erzeugen

dict_name["Key"] = "value"  # Einfügen bzw. ändern eines Elements
dict_name.update({"key": "value"})  # Einfügen bzw. ändern eines Elements
del dict_name["Key"]  # Eintrag löschen
dict_name.pop("key")  # Eintrag löschen
dict_name.popitem()  # löscht den letzten hinzugefügten Eintrag
dict_name.clear()  # Löschen aller Elemente

# gibt den entsprechenden value zurück oder false, falls er nicht existiert
dict_name.get("key")
dict_name.items()  # gibt eine liste mit allen keys und values als tupel zurück
dict_name.keys()  # gibt ein liste mit allen keys zurück
dict_name.values()  # gibt eine liste mit allen values zurück

######################################################################


# https://www.w3schools.com/python/python_ref_dictionary.asp

