#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 2 Terningkast: Tre like verdier

from random import randint

done = False
counter = 0
while not done:
    counter += 1
    throw1 = randint(1,6)
    throw2 = randint(1,6)
    throw3 = randint(1,6)
    print("{:>4d}. kast: {} {} {}".format(counter, throw1, throw2, throw3))
    if throw1 == throw2 and throw2 == throw3:
        done = True
        print("Etter {} kast med tre terninger viste alle terningene verdien {}".format(counter, throw1))
