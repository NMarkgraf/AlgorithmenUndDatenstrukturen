# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Einfaches Rot-13 für Großbuchstaben!

'''

def rot(txt: str) -> str:
    result = ""
    for c in txt.upper():
        if c.isalpha():
            oc = ord(c)
            if oc > ord("N"):
                oc -= 26
            result += chr(oc+13)
        else:
            result += c
    return result

def main():
    print(rot("Test!"))
    print(rot("GRFG!"))

if __name__ == "__main__":
    main()