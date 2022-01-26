#!/usr/bin/env python3

# Oppgave av Stian Knudsen

# 3 Smittespredning

def neste(s, alpha, beta):
    return round(s + alpha*s - beta)

def utvikling(s, alpha, beta, n):
    print("{:<3s}{:>10s}".format("Uke", "Syke"))
    smittede = s
    for i in range(n+1):
        smittede = round(smittede + alpha*smittede - beta)
        if smittede < 0:
            smittede = 0
        print("{:<3d}{:>10d}".format(i, smittede))

def halveringstid(s, alpha, beta):
    if beta > alpha*s:
        ferdig = False
        ukeNummer = 1
        smittede = s
        while not ferdig:
            smittede = round(smittede + alpha*smittede - beta)
            if smittede <= s // 2:
                ferdig = True
                return ukeNummer
            ukeNummer += 1



utvikling(100, 0.2, 25, 10)
print(halveringstid(100, 0.2, 25))

