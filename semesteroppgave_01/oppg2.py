#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2 Kort trukket fra en kortstokk

from random import randint


serieList = ["spar", "kløver", "hjerter", "ruter"]
verdiList = ["ess", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "knekt", "dame", "konge"]

serie = randint(0, 3)
verdi = randint(0, 12)

print("Trekker et tilfeldig kort:")
print("{} {}".format(serieList[serie], verdiList[verdi]))
