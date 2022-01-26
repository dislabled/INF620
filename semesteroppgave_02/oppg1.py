#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 1 Navnelister

def les(kategori):
    """
    Leser inn navn, og returnerer en liste
    """
    navn = input("Første {}: ".format(kategori))
    navne_liste = [navn]
    while navn != "":
        navn = input("Neste {}: ".format(kategori))
        navne_liste.append(navn)
    navne_liste.pop()
    return navne_liste

def skriv_pent(navne_liste):
    """
    Tar imot liste av navn, endrer utforming, og skriver ut
    """
    for navn in navne_liste:
        print(navn.title())

def flett(liste1, liste2):
    """
    Fletter 2 lister
    """
    flettet_liste = []
    index = 0
    while index < max(len(liste1), len(liste2)):
        if index < len(liste1):
            flettet_liste.append(liste1[index])
        if index < len(liste2):
            flettet_liste.append(liste2[index])
        index += 1
    return flettet_liste

def korriger(liste):
    """
    Tar en list med strenger og formaterer den med stor forbokstav
    """
    temp_liste = []
    for element in liste:
        element = element.title()
        temp_liste.append(element)
    return temp_liste

# ---- test oppgv a: ----
# print(les('gruppeleder'))

# ---- test oppgv b: ----
# skriv_pent(["sAndRa", "maTHIlde"])

# ---- test oppgv c: ----
# liste1 = ['Dusan', 'Mathias', 'Eirik', 'Fredrik']
# liste2 = ['Mathilde', 'Sandra']
# print(flett(liste1, liste2))

# ---- test oppgv d: ----
# liste3 = ['sAndRa LEkVe','maTHIlde bloM bergenHEim']
# print(korriger(liste3))
