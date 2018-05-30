# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Teilstringsuche -- Suchen in Zeichenketten

'''


def brute_force(pat: str, txt: str) -> int:
    """Rohe Gewalt.

    :param pat: Suchmuster
    :param txt: Text in dem gesucht werden soll
    :return: Findeposition oder -1, wenn nicht vorhanden.
    """
    m = len(pat)
    n = len(txt)
    for i in range(0, 1+n-m):
        j = 0
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1
        if j == m:
            return i

    return -1

# ============================================================================


def knuth_morris_pratt(pat: str, txt: str) -> int:
    """Algorithmus von Knuth Morris und Pratt.

    :param pat: Suchmuster
    :param txt: Text in dem gesucht werden soll
    :return: Findeposition oder -1, wenn nicht vorhanden.
    """

    def create_dfa(pat: str):
        """Erzeuge einen deterministischen endlichen Automat (dfa).

        :param pat: Suchmuster
        :return: Deterministischer endlicher Automat
        """
        m = len(pat)
        r = 256

        #  Erzeuge einen leeren endlichen Automaten
        new_dfa = [[0 for row in range(0, m)] for col in range(0, r+1)]
        new_dfa[ord(pat[0])][1] = 1
        x = 0
        for j in range(1, m):
            for c in range(0, r):
                new_dfa[c][j] = new_dfa[c][x]
            new_dfa[ord(pat[j])][j] = j + 1
            x = new_dfa[ord(pat[j])][x]
        return new_dfa

    dfa = create_dfa(pat)

    i = 0
    j = 0
    n = len(txt)
    m = len(pat)
    while i < n and j < m:
        j = dfa[ord(txt[i])][j-1]
        i += 1
    if j == m:
        return i-m
    return -1

# ============================================================================


def boyer_moore(pat: str, txt: str) -> int:
    """Algorithmus von Boyer und Moore.

    :param pat: Suchmuster
    :param txt: Text in dem gesucht werden soll
    :return: Findeposition oder -1, wenn nicht vorhanden.
    """
    def create_right(pat: str):
        """Erzeuge Sprungtabelle.

        :param pat: Suchmuster
        """
        m = len(pat)
        r = 256
        right = [-1 for col in range(0, r+1)]
        for j in range(0, m):
            right[ord(pat[j])] = j
        return right

    right = create_right(pat)
    n = len(txt)
    m = len(pat)
    skip = 1
    i = 0
    while i <= n-m:
        skip = 0
        j = m-1
        while j >= 0:
            if pat[j] != txt[i+j]:
                skip = j - right[ord(txt[i+j])]
                if skip < 1:
                    skip = 1
                break
            j -=1
        if skip == 0:
            return i
        i += skip

    return -1

# ============================================================================


def main():
    txt = "Das ist ein einfacher Text um zu Testen ob die Teilstringsuche funktioniert."
    # txt = "1Teil"
    pat = "Teil"
    
    print(brute_force(pat, txt))
    print(knuth_morris_pratt(pat, txt))
    print(boyer_moore(pat, txt))

if __name__ == "__main__":
    main()
