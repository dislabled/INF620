#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 4 Sorteringsgrad av navn

done = False
while done == False:
    sortGrade = 0
    name = input("Skriv inn navn: ").lower()
    if name == "":
        done = True
    else:
        for letter in range(0,len(name)-1):
            if name[letter] <= name[letter+1]:
                sortGrade += 1
        print("{} er et navn med sortingsgrad {}.".format(name, sortGrade))
