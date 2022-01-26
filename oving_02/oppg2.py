#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2.a
# x = 10
print("{:<21}{}".format("x = 10 :", "Datatypen til x er int"))
# x = 10 + 10
print("{:<21}{}".format("x = 10 + 10 :", "Datatypen til x er int"))
# x = 5.5
print("{:<21}{}".format("x = 5.5 :", "Datatypen til x er float"))
# x = 10 + 5.5
print("{:<21}{}".format("x = 10 + 5.5 :", "Datatypen til x er float"))
# x = 5.5 + 5.5
print("{:<21}{}".format("x = 5.5 + 5.5 :", "Datatypen til x er float"))
# x = "abc"
print("{:<21}{}".format("x = \"abc\" :", "Datatypen til x er str"))
# x = "abc" + "5"
print("{:<21}{}".format("x = \"abc\" + \"5\" :", "Datatypen til x er str"))
# x = "abc" + 5
print("{:<21}{}".format("x = \"abc\" + 5 :", "Det er ikke mulig å sette sammen en streng(\"abc\") og et heltall(5)."))
# x = "abc" + str(5)
print("{:<21}{}".format("x = \"abc\" + str(5) :", "Datatypen til x str"))
# x = "5" + 5
print("{:<21}{}".format("x = \"5\" + 5 :", "Det er ikke mulig å sette sammen en streng(\"5\") og et heltall(5)."))
# x = int("5") + 5
print("{:<21}{}".format("x = int(\"5\") + 5 :", "Datatypen til x er int"))
