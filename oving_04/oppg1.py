#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 1 Vokaler

hjelpeStreng = "aeiouyæøå"

def vokaler(streng):
    """
    Returnerer vokalene(streng) i inndata
    """
    delStreng = ""
    for i in streng:
        if i.lower() in hjelpeStreng:
            delStreng += i
    return delStreng

def antallVokaler(streng):
    """
    Returnerer antall vokaler(int) i inndata
    """
    antall = 0
    for i in streng:
        if i.lower() in hjelpeStreng:
            antall += 1
    return antall

innStreng = input("Legg inn streng: ")
print(vokaler(innStreng))
print(antallVokaler(innStreng))
