#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Türme von Hanoi

'''

def printTuerme(tuerme):
    pass
    """
    print("A: ", tuerme[0])
    print("B: ", tuerme[1])
    print("C: ", tuerme[2])
    print("###################################")
    """

def hanoi(n, quelle, ziel, extern):
  if n == 1:
      print(quelle, "->", ziel)
      tuerme[ziel-1].append(tuerme[quelle-1].pop())
      printTuerme(tuerme)
  else:
      hanoi(n-1, quelle, extern, ziel)
      hanoi(  1, quelle, ziel, extern)
      hanoi(n-1, extern, ziel, quelle)
      

def hanoiIterative(n, quelle, ziel, extern):
    stack = []
    stack.append(quelle)
    stack.append(ziel)
    stack.append(extern)
    stack.append(n)
    while True:
        while n > 1:
            stack.append(quelle)
            stack.append(ziel)
            stack.append(extern)
            stack.append(n)
            n -= 1
            extern, ziel = ziel, extern  # swap
        print(quelle, "->", ziel)
        tuerme[ziel-1].append(tuerme[quelle-1].pop())
        printTuerme(tuerme)
        n = stack.pop()
        extern = stack.pop()
        ziel = stack.pop()
        quelle = stack.pop()
        if not stack:
            break
        print(quelle, "->", ziel)
        tuerme[ziel-1].append(tuerme[quelle-1].pop())
        printTuerme(tuerme)
        n -= 1
        quelle, extern = extern, quelle
        

tuerme = [[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], []]
A = 1
B = 2
C = 3
n = len(tuerme[0])
printTuerme(tuerme)
hanoi(n, A, B, C)
print("---------------------------------")
tuerme = [[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], []]
A = 1
B = 2
C = 3
n = len(tuerme[0])
printTuerme(tuerme)
hanoiIterative(n, A, B, C)

