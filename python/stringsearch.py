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

    for i in range(0, n-m+1):
        j = 0  # Anzahl der erkanten Zeichen des Suchmusters
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1
        if j == m:  # Suchmuster gefunden!
            return i
    return -1

# ============================================================================


def brute_force_sentinal(pat: str, txt: str) -> int:
    """Rohe Gewalt (mit Sentinaltechnik).

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

    a = txt + pat  # Sentinal am Ende anhängen!

    i = 0
    while True:
        j = 0
        while j < m:
            if a[i+j] != pat[j]:
                break
            j += 1
        if j == m:  # Suchmuster gefunden!
            if i < n:  # Suchstelle gefunden!
                return i
            else:  # Sentinal gefunden!
                return -1
        i += 1

# ============================================================================


def knuth_morris_pratt(pat: str, txt: str) -> int:

    def init_next(pat: str):
        next = [-1 for col in range(0, len(pat)+1)]
        i = 0
        j = -1
        m = len(pat)
        next[0] = -1
        while i < m:
            while j >= 0and pat[i] != pat[j]:
                j = next[j]
            i += 1
            j += 1
            next[i] = j
        return next

    next = init_next(pat)
    m = len(pat)
    n = len(txt)

    a = txt + pat  # Sentinal anhängen

    i = 0
    j = 0

    while j < m:
        while j >= 0 and a[i] != pat[j]:
            j = next[j]
        i += 1
        j += 1

    if i-m < n:
        return i-m  # Suchstelle gefunden!
    else:
        return -1  # Sentinal gefunden!

# ============================================================================


def knuth_morris_pratt_dfa(pat: str, txt: str) -> int:
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
            j -= 1
        if skip == 0:
            return i
        i += skip

    return -1
# ============================================================================


def boyer_moore_sentinal(pat: str, txt: str) -> int:
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
    a = txt + pat  # Sentinal!
    n = len(txt)
    m = len(pat)
    i = -1
    skip = 1
    while skip!=0:
        i += skip
        skip = 0
        j = m-1
        while j >= 0:
            if pat[j] != a[i+j]:
                skip = j - right[ord(a[i+j])]
                if skip < 1:
                    skip = 1
                break
            j -= 1
    if i < n:
        return i
    else:
        return -1

# ============================================================================


def rabin_karp(pat: str, txt: str, monte_carlo: bool=True) -> int:
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
    #q = 2 ** 31 -1  # 8. Mersenne-Primzahl zum Exponenten 31!
                    # Damit ist mod q das selbe wie and q!
    rn = 8
    r = 1 <<  rn # =256  Größe des Zeichenbereichs (ASCII = 256, Unicode 65535 (?))

    def get_pot(r: int, q: int, m: int) -> int:
        """Erzeuge ein inverses Element.

            $pot = r^(m-1) mod q$

        :param r: Größe des Zeichenbereichs (ASCII=256)
        :param q: (Primzahl-)Modulus
        :param m: Länge des Suchmusters
        """
        pot = 1
        for i in range(1, m):
            for j in range(0, 8):
                pot <<= 1
                if pot > q:
                    pot -= q
        return pot

    def check_monte_carlo(pat: str, ctxt: str):
        """Prüfe ob pat wirklich gleich ctxt ist.

        :param pat: Suchmuster
        :param ctxt: Textausschnitt
        :return: TRUE falls gleich, sonst FALSE
        """
        # Monte Carlo: einfach nur TRUE liefern!
        return True

    def check_las_vegas(pat: str, ctxt: str):
        """Prüfe ob pat wirklich gleich ctxt ist.

        :param pat: Suchmuster
        :param ctxt: Textausschnitt
        :return: TRUE falls gleich, sonst FALSE
        """
        # "Las Vegas": Wirklich testen!
        for i in range(0, len(pat)):
          if pat[i] != ctxt[i]:
              return False
        return True


    def hash_fkt(key: str, r: int, q: int) -> int:
        """Hashfunktion.

        :param key: Schlüssel
        :param r: Größe des Zeichenbereichs
        :param q: Modulus
        :return:
        """
        h = 0
        for i in range(len(key)):
            for j in range(0, rn):
                h <<= 1
                if h > q:
                    h -= q
            h += ord(key[i])
            if h > q:
                h -= q
        return h


    def update_hash(old_hash: object, old_char: object, new_char: object, q: object, pot: object, rn: object) -> object:
        """Aktualisiere den Hashwert.

        :param old_hash: old hash
        :param old_char: character to remove from hash (ord(txt[i - m])
        :param new_char: character to add to hash (ord(txt[i]))
        :return: new hash
        """
        new_hash = old_hash
        tmp = (pot * old_char) % q
        if tmp > new_hash:
            new_hash += q
        new_hash -= tmp
        if new_hash > q:
            new_hash -= q
        new_hash = (new_hash << rn) % q
        new_hash += new_char
        if new_hash > q:
            new_hash -= q
        return new_hash


    if monte_carlo:
        check = check_monte_carlo
    else:
        check = check_las_vegas

    n = len(txt)
    m = len(pat)
    pot = get_pot(r, q, m)

    pat_hash = hash_fkt(pat, r, q)
    txt_hash = hash_fkt(txt[0:m], r, q)

    i = m
    while i < n:
        if pat_hash == txt_hash:
            if check(pat, txt[i-m:i]):
                return i-m
        """ Variante 1:
        txt_hash = (txt_hash + (q - (pot * ord(txt[i-m]) % q) % q) %q) % q
        txt_hash = (((txt_hash * r) % q) + ord(txt[i])) % q
        """
        """Variante 2:
        tmp = (pot * ord(txt[i-m])) % q
        txt_hash = (txt_hash + q - tmp) % q
        txt_hash = (txt_hash * r) % q
        txt_hash = (txt_hash + ord(txt[i])) % q
        """
        """Variante 3:
        tmp = (pot * ord(txt[i - m])) % q
        if tmp > txt_hash:
            txt_hash += q
        txt_hash -= tmp
        txt_hash *= r
        txt_hash %= q
        txt_hash += ord(txt[i])
        """
        txt_hash = update_hash(txt_hash, ord(txt[i - m]), ord(txt[i]), q, pot, rn)
        i += 1
    return -1

def rabin_karp_las_vegas(pat: str, txt: str) -> int:
    return rabin_karp(pat, txt, monte_carlo=False)

def setup(pat="@norman_markgraf") -> str:
    import urllib.request
    webseite = "http://sefiroth.net/nab/"
    t = urllib.request.urlopen(webseite)
    return pat, t.read().decode("utf-8").encode("ascii", "ignore").decode("utf-8")

def timing_test(show_msg="", method=None, setup_routine=None):
    import timeit
    rep = 5
    print(show_msg, end="", flush=True)
    t = timeit.Timer(""+method+"(pat, txt)", setup="from __main__ import setup,"+method+"; pat, txt = setup();")
    # print("%8.7f" % (sum(t.repeat(rep, 100)) / rep))
    print("%8.7f" % (min(t.repeat(rep, 20))))
    print("", end="", flush=True)

def correction_test(show_msg="", method=None):
    print(show_msg, end="", flush=True)
    pat, txt = setup()
    print(eval(method+"(pat, txt)"))

def test(show_msg="", method=None, setup_routine=None):
    correction_test(show_msg, method)
    timing_test(show_msg, method, setup_routine)

def main():
    # txt = "Das ist ein einfacher Text um zu Testen ob die Teilstringsuche funktioniert."
    pat = "Markgraf"

    test("Bruce force             :\t", "brute_force", setup)
    test("Bruce force   (Sentinal):\t", "brute_force_sentinal", setup)
    test("Knuth-Morris-Pratt      :\t", "knuth_morris_pratt", setup)
    test("Knuth-Morris-Pratt (dfa):\t", "knuth_morris_pratt_dfa", setup)
    test("Boyer-Moore             :\t", "boyer_moore", setup)
    test("Boyer-Moore   (Sentinal):\t", "boyer_moore_sentinal", setup)
    test("Rabin-Karp (Monte Carlo):\t", "rabin_karp", setup)
    test("Rabin-Karp   (Las Vegas):\t", "rabin_karp_las_vegas", setup)
    """
    print("Bruce force             :\t", brute_force(pat, txt))
    print("Bruce force   (Sentinal):\t", brute_force_sentinal(pat, txt))
    print("Knuth-Morris-Pratt      :\t", knuth_morris_pratt(pat, txt))
    print("Knuth-Morris-Pratt (dfa):\t", knuth_morris_pratt_dfa(pat, txt))
    print("Boyer-Moore             :\t", boyer_moore(pat, txt))
    print("Boyer-Moore   (Sentinal):\t", boyer_moore_sentinal(pat, txt))
    print("Rabin-Karp (Monte Carlo):\t", rabin_karp(pat, txt))
    print("Rabin-Karp   (Las Vegas):\t", rabin_karp_las_vegas(pat, txt)
    """

if __name__ == "__main__":
    main()
