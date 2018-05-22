#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Ackermannfunktion und Sudanfunktion

'''

def ackermann(m, n):
    """Ackermannfunktion.
    
    Definition nach Rózsa Péter. vgl. https://de.wikipedia.org/wiki/Ackermannfunktion
    """
    if m == 0:
        return n + 1
    else:
        if n == 0:
            return ackermann(m-1, 1)
        else:
            return ackermann(m-1, ackermann(m, n-1))
    

def ackermann2(m, n):
    """Ackermannfunktion teilweise iterativ.
    """
    while m != 0:
        if n == 0:
            n = 1
        else:
            n = ackermann2(m, n-1)
        m -= 1
    return n + 1
    

def sudan(n, x, y):
    """Sudanfunktion.
    
    vlg. https://de.wikipedia.org/wiki/Sudanfunktion
    """
    if n == 0:
        return x + y
    else: 
        if (y == 0):
            return x
        else:
            return sudan(n-1, sudan(n,x, y-1), sudan(n,x,y-1) + y)

print(ackermann(2, 500))

#print(sudan(2,2,2))
