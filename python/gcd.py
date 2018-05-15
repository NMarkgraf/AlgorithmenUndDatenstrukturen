'''
Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Der Euklidische Algorithmus zur Berechung des größten gemeinsamen Teilers
zweier Zahlen.

'''
import sys

def gcd_simple(u, v):
    """ (Einfacher) Euklidscher Algorithmus

    Euklidischer Algorithmus zu Bestimmung des größten gemeinstamen 
    Teilers (ggT) mit Hilfe einer einfacher Subtraktion.

    :param u: ein Integerwert
    :param v: ein Integerwert
    :return: der größte gemeinsame Teiler von u und v
    """
    while (u > 0):
        if (v > u):
            u, v = v, u
        u = u - v
    return v


def gcd(u, v):
    """ Euklidscher Algorithmus

    Euklidischer Algorithmus zu Bestimmung des größten gemeinstamen 
    Teilers (ggT) mit Hilfe der Modulorechnung.

    :param u: ein Integerwert
    :param v: ein Integerwert
    :return: der größte gemeinsame Teiler von u und v
    """
    while (u > 0):
        if (v > u):
            u, v = v, u
        u %= v
    return v


def main():
    if len(sys.argv) == 3:
        u = int(sys.argv[1])
        v = int(sys.argv[2])
        ggT = gcd(u, v)
        print("ggT("+str(u)+", "+str(v)+") = "+str(ggT))
    else:
        print("usage: python gcd.py u v")


if __name__ == "__main__":
    main()
