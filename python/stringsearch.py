# -*- coding: utf-8 -*-
'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Teilstringsuche -- Suchen in Zeichenketten

'''


def brute_force(pat: str, txt: str) -> int:
    """Rohe Gewalt.

    Anzahl der Operationen:

     Garantiert  |  Typisch
    -------------+-----------
     M * N       | 1,1 * N

    Zusatzspeicher: 1


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

    Anzahl der Operationen:

     Garantiert  |  Typisch
    -------------+-----------
     2 * N       | 1,1 * N

    Zusatzspeicher: M * R

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
        new_dfa[ord(pat[0])][0] = 1
        x = 0
        for j in range(1, m):
            cj = ord(pat[j])
            for c in range(0, r):
                new_dfa[c][j] = new_dfa[c][x]
            new_dfa[cj][j] = j + 1
            x = new_dfa[cj][x]
        return new_dfa

    dfa = create_dfa(pat)

    i = 0
    j = 0
    n = len(txt)
    m = len(pat)
    while i < n and j < m:
        j = dfa[ord(txt[i])][j]
        i += 1
    if j == m:
        return i-m
    return -1

# ============================================================================


def boyer_moore(pat: str, txt: str) -> int:
    """Algorithmus von Boyer und Moore.

    Anzahl der Operationen:

     Garantiert  |  Typisch
    -------------+-----------
     3 * N       | N / M

    Zusatzspeicher: R

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


def rabin_karp(pat: str, txt: str) -> int:
    """Algorithmus von Rabin Karp (Fingerprint-Algorithmus).

    Anzahl der Operationen:

     Garantiert  |  Typisch
    -------------+-----------
     7 * N       | 7 * N

    Zusatzspeicher: 1

    :param pat: Suchmuster
    :param txt: Text in dem gesucht werden soll
    :return: Findeposition oder -1, wenn nicht vorhanden.
    """

    q = 8388593  # Primzahl / Modulus
    r = 256

    def get_inv(r: int, q: int, m: int) -> int:
        """Erzeuge ein inverses Element.

            $inv = r^(m-1) mod q$

        :param r: Größe des Zeichenbereichs (ASCII=256)
        :param q: (Primzahl-)Modulus
        :param m: Länge des Suchmusters
        """
        inv = 1
        for i in range(1,m):
            inv = (inv * r) % q
        return inv


    def check(pat: str, ctxt: str):
        """Prüfe ob pat wirklich gleich ctxt ist.

        :param pat: Suchmuster
        :param ctxt: Textausschnitt
        :return: TRUE falls gleich, sonst FALSE
        """
        # Monte Carlo: einfach nur TRUE liefern!
        return True
        # Las Vegas: Wirklich testen!
        # return pat == ctxt


    def hash(key: str, r: int, q: int) -> int:
        """Hashfunktion.

        :param key: Schlüssel
        :param r: Größe des Zeichenbereichs
        :param q: Modulus
        :return:
        """
        h = 0
        for i in range(len(key)):
            h = (h * r + ord(key[i])) % q
        return h

    n = len(txt)
    m = len(pat)
    inv = get_inv(r, q, m)

    pat_hash = hash(pat, r, q)
    txt_hash = hash(txt[0:m], r, q)

    i = m
    while i < n:
        if pat_hash == txt_hash:
            if check(pat, txt[i-m:i]):
                return i-m
        txt_hash = (txt_hash + q - (inv*ord(txt[i-m]) % q)) % q
        txt_hash = (txt_hash * r + ord(txt[i])) % q
        i += 1
    return -1


def main():
    txt = "Das ist ein einfacher Text um zu Testen ob die Teilstringsuche funktioniert."
    pat = "Teil"
    
    print("Bruce force       :\t", brute_force(pat, txt))
    print("Knuth-Morris-Pratt:\t", knuth_morris_pratt(pat, txt))
    print("Boyer-Moore       :\t", boyer_moore(pat, txt))
    print("Rabin-Karp        :\t", rabin_karp(pat, txt))

if __name__ == "__main__":
    main()
