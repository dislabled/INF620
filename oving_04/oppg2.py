#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2 Terninger og spill
from random import randint


def terninger(n):
    """
    Kaster antall(n) terninger, og returnerer sum
    """
    sum = 0
    for i in range(0, n):
        sum += randint(1, 6)
    return sum

def stigeSpill(navn, n):
    """
    Tar imot navn, og lar spiller kaste (n) terninger
    """
    poeng = 0
    ferdig = False
    while ferdig == False:
        svar = input("{} har {} poeng. Flere kast (j/n)? ".format(navn, poeng))
        if svar[0].lower() == "j":
            poeng = terninger(n)
            print("{} fikk {} poeng med {} terninger".format(navn, poeng, n))
        else:
            ferdig = True
            print("Resultat for {}: {}".format(navn, poeng))
    return poeng

def turnering():
    """
    Skriver ut vinner av turneringen
    """
    terninger = int(input("Antall terninger: "))
    navn = input("Første spiller (avslutt med tom streng): ")
    vinnerSum = 0
    leder = navn
    while navn != "":
        poeng = stigeSpill(navn, terninger)
        if poeng > vinnerSum:
            vinnerSum = poeng
            leder = navn
            navn = input("{} leder med {} poeng. Neste spiller (avslutt med en tom streng): ".format(leder, vinnerSum))
        else:
            navn = input("{} leder med {} poeng. Neste spiller (avslutt med en tom streng): ".format(leder, vinnerSum))
    print("{} vant turneringen med {} poeng.".format(leder, vinnerSum))


turnering()

