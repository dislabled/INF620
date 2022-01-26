#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 1 Beregning av eksamenskarakter

poengSum = int(input("Legg inn Poengsum: "))

if poengSum > 100 or poengSum < 0:
    print("Poengsummen er utenfor skalaen!")
    exit()
if poengSum >= 90:
    print("Karakteren er: A")
elif poengSum >= 80:
    print("Karakteren er: B")
elif poengSum >= 60:
    print("Karakteren er: C")
elif poengSum >= 50:
    print("Karakteren er: D")
elif poengSum >= 40:
    print("Karakteren er: E")
elif poengSum >= 0:
    print("Karakteren er: F")
