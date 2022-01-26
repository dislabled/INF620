#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 1 Sjekk av gyldig passord

password = input("skriv inn et passord: ")

lCaseLetter = False
uCaseLetter = False
number = False
specialChar = False

for i in password:
    if i.islower():
        lCaseLetter = True
    elif i.isupper():
        uCaseLetter = True
    elif i.isdigit():
        number = True
    else:
        specialChar = True

if len(password) >= 8 and lCaseLetter and uCaseLetter and number and specialChar:
    print("Gyldig Passord")
else:
    print("Ugyldig Passord")
