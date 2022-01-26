#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 4.a

number1, number2 = int(input("Skriv inn 2 heltall: ")), int(input(" " * 21))
print("-" * 25)
print("{:<15} {:<5}".format("Sum:", number1 + number2))
print("{:<15} {:<5}".format("Differanse:", number1 - number2))
print("{:<15} {:<5}".format("Produkt:", number1 * number2))
print("{:<15} {:<5}".format("Gjennomsnitt:", (number1 + number2) / 2))
print("{:<15} {:<5}".format("Distanse:", abs(number1 - number2)))
print("{:<15} {:<5}".format("Maksimum:", max(number1, number2)))
print("{:<15} {:<5}".format("Minimum:", min(number1, number2)))
print("-" * 25)
