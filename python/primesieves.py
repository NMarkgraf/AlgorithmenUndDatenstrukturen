'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Primzahlsiebe:

1. Sieb des Eratosthenes
    (vgl: https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes)

2. Sieb von Sudaram
    (vgl:   https://en.wikipedia.org/wiki/Sieve_of_Sundaram oder
            http://lebendom.com/article/sieb-von-sundaram)


'''

import sys
import math
import timeit


def eratosthenes(n):
    """Das Sieb des Eratosthenes.

    Erzeugt eine Liste von Primzahlen bis zur Obergrenze *n*

    :param: n Obergrenze des Siebs
    """
    s = set(range(1, n))
    nn = int(math.floor(math.sqrt(n))+1)
    s.discard(1)

    for i in range(1, nn):
        if i in s:
            for k in range(i*i, n+1, i):
                if k < n:
                    s.discard(k)
    r = []
    for i in range(1, n):
        if i in s:
            r.append(i)
    return r

# ============================================================================


def sundaram(n):
    """Das Sieb von Sundaram.

    Erzeugt eine Liste von Primzahlen bis zur Obergrenze *n*

    :param: n Obergrenze des Siebs
    """
    nn = int(math.floor((n-2)/2) + 1)
    s = set(range(1, nn))
    for i in range(1, nn+1):
        j = i
        idx = i+j+2*i*j
        while (idx < nn):
            s.discard(idx)
            j += 1
            idx = i+j+2*i*j
    r = [2]
    for i in range(1, nn):
        if i in s:
            r.append(2*i+1)
    return r

# ============================================================================


def main():
    """Hauptroutine

    Berechne die ersten n Primzahlen mit dem Sieb des Eratosthenes, oder
    mit Hilfe des Siebs von Sudaram ("-s" als Option).
    """
    t = -1
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        t = 0
    else:
        if len(sys.argv) == 3:
            n = int(sys.argv[2])
            t = (sys.argv[1] == "-s")
    if t < 0:
        print("usage: python primesieves.py [-s] n")
    else:
        if t == 1:
            print("Sieb von Sundaram:")
            print(sundaram(n))
        else:
            print("Sieb des Eratosthenes")
            print(eratosthenes(n))


if __name__ == "__main__":
    main()
