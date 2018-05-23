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
    

def ackermannIterative(m, n):
    stack = []
    stack.append(m)
    while stack:
        m = stack.pop()
        if m == 0:
            n += m+1
        else:
            if n == 0:
                n = 1
                m = m - 1
                stack.append(m)
            else:
                stack.append(m-1)
                stack.append(m)
                n -= 1
    return n


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

print(ackermannIterative(4, 1))

#print(sudan(2,2,2))
