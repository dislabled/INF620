#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 3 Terningkast: Tre seksere

from random import randint

done = False
counter = 0
throw1 = 0
throw2 = 0
throw3 = 0
while not done:
    counter += 1
    if throw1 != 6:
        throw1 = randint(1,6)
    if throw2 != 6:
        throw2 = randint(1,6)
    if throw3 != 6:
        throw3 = randint(1,6)
    print("{:>4d}. kast: {} {} {}".format(counter, throw1, throw2, throw3))
    if throw1 == 6 and throw2 == 6 and throw3 == 6:
        done = True
        print("Etter {} kast med tre terninger viste alle terningene verdien {}".format(counter, throw1))
