#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2 Yatzy
from random import randint
from matplotlib import pyplot


def kast(n):
    """
    Returnerer (n)antall kast med terninger
    """
    kast = []
    for i in range(n):
        kast.append(randint(1, 6))
    return kast

def finn_antall(terninger):
    """
    Returnerer antall av hver terningverdi som en liste
    """
    antall_liste = [0,0,0,0,0,0]
    for i in range(6):
        for j in range(len(terninger)):
            if i+1 == terninger[j]:
                antall_liste[i] += 1
    return antall_liste

def finn_flest(antall):
    """
    Finner og returnerer hvilken terningverdi som
    forekommer flest ganger
    """
    return max(antall, key = antall.count)

def nytt_kast(terninger, spar):
    """
    Returnerer liste med nytt kast foruten sparte verdier
    """
    for i in range(len(terninger)):
        if terninger[i] != spar:
            terninger[i] = (randint(1,6))
    return terninger

def yatzy(n, utskrift=False):
    """
    Spiller Yatzy, returnerer antall kast til yatzy
    """
    hånd = kast(n)
    valg = finn_flest(hånd)
    if utskrift:
        print(hånd)
    antall_kast = 1
    while len(set(hånd)) != 1:
        nytt_kast(hånd, valg)
        antall_kast += 1
        if utskrift:
            print(hånd)
    return antall_kast

def plott_funksjon():
    """
    Returnerer en plot av hvor mange kast før yatzy på
    1 - 100 terninger
    """
    omganger = []
    for i in range(1, 100):
        omganger.append(yatzy(i))
    pyplot.plot(range(1, 100), omganger)
    pyplot.show()


e_oppgave = input("Ekstraoppgave (ja/nei)")
if e_oppgave[0].lower() == "j":
    plott_funksjon()
else:
    antall_terninger = int(input("Antall terninger: "))
    print("Yatzy med {} terninger på {} kast.".format(
        antall_terninger, yatzy(antall_terninger, utskrift=True)))


