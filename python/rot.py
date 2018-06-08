# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Einfaches ROT-13 für Buchstaben.

'''


def rot(txt: str) -> str:
    result = ""
    for c in txt:
        if c.isalpha():
            oc = ord(c)
            if c.upper() > "M":
                oc -= 26
            result += chr(oc + 13)
        else:
            result += c
    return result

def main():
    print(rot("Test!"))
    print(rot("Grfg!"))
    txt = rot("Und es begab sich aber zu der Zeit, als ein Gespraech begann ueber den Sinn und den Unsinn von Statistik!")
    print(txt)
    print(rot(txt))

if __name__ == "__main__":
    main()