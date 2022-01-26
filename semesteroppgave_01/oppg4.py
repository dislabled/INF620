#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 4 Beregning av ukedag

uken = ["mandag", "tirsdag", "onsdag",
        "torsdag", "fredag", "lørdag", "søndag"]

dagNå = uken.index(input("Hvilken dag er det idag? ").lower())
dagerTil = int(input("Hvor mange dager er det til den store dagen? "))
print("Den store dagen faller på en {}".format(uken[(dagNå + dagerTil) % 7]))

