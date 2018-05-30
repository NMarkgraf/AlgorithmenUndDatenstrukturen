'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Ein paar Sortierverfahren inkl. kleiner Demonstration

'''


from abc import ABC, abstractmethod


class Sorter(ABC):

    def __init__(self):
        self._name = None

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    @abstractmethod
    def sort(self, feld):
        pass

    def __test_simple(self):
        testfeld = [1, 3, 5, 3, 7, 10, 4, 2, 4]
        print(testfeld)
        self.sort(testfeld)
        print(testfeld)

    def __test_random(self):
        from random import randint, seed
        seed(2009)
        n = 30  # Feldgröße
        max_value = 2*n  # Maximaler Wert im Feld (0..max_value)
        testfeld = [0] * n
        for i in range(n):
            testfeld[i] = randint(0, max_value)

        print(testfeld)
        self.sort(testfeld)
        print(testfeld)

    def __test_random_multi(self):
        from random import randint, seed
        seed(2009)
        n = 30  # Feldgröße
        max_value = 2*n  # Maximaler Wert im Feld (0..max_value)
        testfeld = [0] * n
        for i in range(n):
            testfeld[i] = randint(0, max_value)

        print(testfeld)
        self.sort_multitasking(testfeld)
        print(testfeld)


    def test(self):
        print(self)
        # self.__test_simple()
        self.__test_random()

    def test_multitasking(self):
        print(self," multitasking",)
        # self.__test_simple()
        self.__test_random_multi()

# ============================================================================


class GnomeSort(Sorter):
    """
    Charakteristik: stabil und in place

    Komplexität:

    Best Case | Average Case | Worst Case
    ----------+--------------+-----------
     O(n)     |  O(n^2)      | O(n^2)


    Bemerkung:
        - Dieses Sortierverfahren wurde zunächst Stupid Sort genannt.

    Quellen:
        - http://sina.sharif.edu/~azad/stupid-sort.PDF (noch als Stupid Sort)
        - https://dickgrune.com/Programs/gnomesort.html
        - https://en.wikipedia.org/wiki/Gnome_sort
    """

    def __init__(self):
        super().__init__()
        self._name = "Gnomesort"

    def sort(self, feld):
        i = 0
        n = len(feld)
        while i < n:
            if i and feld[i] < feld[i - 1]:
                feld[i], feld[i - 1] = feld[i - 1], feld[i]
                i -= 1
            else:
                i += 1
        return feld

# ============================================================================

    
class BubbleSort(Sorter):
    """Bubblesort.


    Charakteristik: stabil und in place

    Komplexität:

    Best Case | Average Case | Worst Case
    ----------+--------------+-----------
     O(n)     |  O(n^2)      | O(n^2)


    Bemerkungen:
        - https://youtu.be/lyZQPjUT5B4 (Bubblesort als Ungarischer Volkstanz)

    Links:
        - https://de.wikipedia.org/wiki/Bubblesort
        - https://en.wikipedia.org/wiki/Bubble_sort

    """

    def __init__(self):
        super().__init__()
        self._name = "Bubblesort"

    def sort(self, feld):
        for passesLeft in range(len(feld)-1, 0, -1):
            for index in range(passesLeft):
                if feld[index] > feld[index + 1]:
                    feld[index], feld[index + 1] = feld[index + 1], feld[index]
        return feld


class CocktailSort(Sorter):
    """Cocktail (oder auch Shaker) Sort.

    Charakteristik: stabil und in place

    Komplexität:

    Best Case | Average Case | Worst Case
    ----------+--------------+-----------
     O(n)     |  O(n^2)      | O(n^2)

     Bemerkung:
        - BiDi(rektionales) Bubblesort. Daher auch BiDiBubblesort genannt.

    """

    def __init__(self):
        super().__init__()
        self._name = "Cocktailsort"

    def __bubble_up(self, feld, l, r):
        swapped = False
        for i in range(l, r):
            if feld[i] > feld[i + 1]:
                feld[i], feld[i + 1] = feld[i + 1], feld[i]
                swapped = True
        return swapped
        
    def __bubble_down(self, feld, l, r):
        swapped = False
        for i in range(l, r, -1):
            if feld[i] < feld[i - 1]:
                feld[i], feld[i - 1] = feld[i - 1], feld[i]
                swapped = True
        return swapped
        
    def __split(self, feld, l, r):
        q = int((r-l+1) / 2)
        for i in range(l+q, r): 
            # do parallel: 
            if feld[i-q] > feld[i]:
                feld[i], feld[i - q] = feld[i - q], feld[i]
        return r-q

    def sort_multitasking(self, feld):
        l = 0
        r = len(feld)
        while l < r:
            q = self.__split(feld, l, r)
            # do parallel:
            self.__bubble_down(feld, q, l)
            l += 1
            r -= 1
            self.__bubble_up(feld, q, r)

    def sort(self, feld):
        for k in range(len(feld) - 1, 0, -1):
            swapped = False
            swapped += self.__bubble_down(feld, k, 0)
            swapped += self.__bubble_up(feld, 0, k)
            """
            for i in range(k, 0, -1):
                if feld[i] < feld[i - 1]:
                    feld[i], feld[i - 1] = feld[i - 1], feld[i]
                    swapped = True

            for i in range(k):
                if feld[i] > feld[i + 1]:
                    feld[i], feld[i + 1] = feld[i + 1], feld[i]
                    swapped = True
            """
            if not swapped:
                return feld

# ============================================================================


class ShellSort(Sorter):
    """ShellSort - Sortieren durch kluges Einsetzen über Distanz(folg)en.

    Charakteristik: instabil und in place

    Komplexität:

    Best Case | Average Case   | Worst Case     | Distanzfolge
    ----------+----------------+----------------+------------------------
              |  O(n^2)        |  O(n^2)        | Orginalfolge von Shell
              |  O(n^1,5)      |  O(n^1,5)      | Folge von Hibbard
              |  O(n log(n)^2  |  O(n log(n)^2  | Folge von Pratt


    Bemerkungen:
        - Shellsort ist ein von Donald L. Shell im Jahr 1959 entwickeltes
          Sortierverfahren, welches auf dem Insertionsort basiert.
        - Die Komplexität hängt entscheidend von der Distanzfolge ab!
          Hier implementiert ist die Orginalfolge von Shell.
          (1, 2, 4, 8, 16, ... 2^k)
        - Mit der Folge 1, 3, 7, 15, 31, 63, …, 2k - 1 von Hibbard wird
          eine Komplexität von O(n^1,5) erreicht.

    Quellen:
        - https://en.wikipedia.org/wiki/Shellsort
        - https://de.wikipedia.org/wiki/Shellsort
        - http://www.inf.fh-flensburg.de/lang/algorithmen/sortieren/shell/shellen.htm
        - https://www.cs.wcupa.edu/rkline/ds/shell-comparison.html

    """
    def __init__(self):
        super().__init__()
        self._name = "Shellsort"

    def sort(self, feld):
        gap = len(feld) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(feld)):
                val = feld[i]
                j = i
                while j >= gap and feld[j - gap] > val:
                    feld[j] = feld[j - gap]
                    j -= gap
                feld[j] = val
            gap //= 2
        return feld

# ============================================================================


class InsertSort(Sorter):
    """InsertSort - Sortieren durch direktes Einfügen.


    Charakteristik: stabil und in place

    Komplexität:

    Best Case | Average Case | Worst Case
    ----------+--------------+-----------
     O(n)     |  O(n^2)      | O(n^2)


    Bemerkungen:
        - Wurde von Robert Sedgewick um eine Sentinal-Technik erweitert und
          verbessert.
        - Wurde von Donald L. Shell durch die Idee verbessert, statt
          benachbarter Elemente zu vegleichen, nimmt man Elemente bestimmter
          Abstände und verringert diese Abstände mit jedem Durchlauf.
          Das Verfahren heißt *ShellSort* und ist nicht mehr stabil.

    Quelle:
        - https://de.wikipedia.org/wiki/Insertionsort

    """
    def __init__(self):
        super().__init__()
        self._name = "Insertsort"

    def sort(self, feld):
        for removed_index in range(1, len(feld)):
            removed_value = feld[removed_index]
            insert_index = removed_index
            while insert_index > 0 and feld[insert_index - 1] > removed_value:
                feld[insert_index] = feld[insert_index - 1]
                insert_index = insert_index - 1
            feld[insert_index] = removed_value
        return feld


def main():
    bubblesort = BubbleSort()
    bubblesort.test()

    gnomesort = GnomeSort()
    gnomesort.test()

    cocktailsort = CocktailSort()
    cocktailsort.test()
    cocktailsort.test_multitasking()

    shellsort = ShellSort()
    shellsort.test()

    insertsort = InsertSort()
    insertsort.test()


if __name__ == "__main__":
    main()
