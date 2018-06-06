# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

soundex - Algorithmus

'''

def soundex_alt(txt: str) -> str:
    """

    :param txt:
    :return:
    """
    dic = { "B" : "1", "C" : "2", "D" : "3", "F" : "1", "G" : "2",
            "J" : "2", "K" : "2", "L" : "4", "M" : "5", "N" : "5",
            "P" : "1", "Q" : "1", "R" : "6", "S" : "2", "T" : "3",
            "V" : "1", "X" : "2", "Z" : "2"
    }
    txtc = txt.upper()
    sndex = lc = txtc[0]
    cnt = 1
    for i in range(1, len(txtc)):
        c = txtc[i]
        if lc != c:
            if c in dic:
                sndex += dic[c]
                cnt +=1
        if cnt > 4:
            break

    return (sndex + "000")[0:4]


def soundex(txt: str) -> str:
    """Liefert den Soundex-Code für ein Wort.

    :param txt: Eind Wort (ohne Leer- und Sonderzeichen!)
    :return: Soundex-Code zu "txt"
    """
    tab = "01230120022455012623010202"
    txtc = txt.upper()
    sndex = lc = txtc[0]
    cnt = 2
    for i in range(2, len(txtc)):
        if cnt > 4:
            break
        c = txtc[i]
        if c != lc:
            lc = c
            c = tab[ord(c) - ord("A")]
            if c != "0":
                sndex += c
                cnt += 1
    return (sndex+"000")[0:4]

def main():
    wort = "Markgraf"
    print(wort, "\t", soundex(wort))
    wort = "Merkgrund"
    print(wort, "\t", soundex(wort))
    wort = "Merkstand"
    print(wort, "\t", soundex(wort))
    wort = "Marksand"
    print(wort, "\t", soundex(wort))
    wort = "Markquard"
    print(wort, "\t", soundex(wort))
    wort = "Markword"
    print(wort, "\t", soundex(wort))

if __name__ =="__main__":
    main()