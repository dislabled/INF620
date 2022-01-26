#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2 Kort trukket fra en kortstokk

from random import randint


verdi01 = randint(1, 6)
verdi02 = randint(1, 6)
verdi03 = randint(1, 6)
verdiMin = min(verdi01, verdi02, verdi03)
verdiMax = max(verdi01, verdi02, verdi03)
verdiMedian = (verdi01 + verdi02 + verdi03) - verdiMin - verdiMax

print("{:<15s} {}".format("Minste verdi: ", verdiMin))
print("{:<15s} {}".format("Median: ", verdiMedian))
print("{:<15s} {}".format("Største verdi: ", verdiMax))
if verdiMax - verdiMedian == verdiMedian - verdiMin:
    print("Medianen ligger midt mellom minste og største verdi")
else:
    print("Medianen ligger ikke midt mellom minste og største verdi")
