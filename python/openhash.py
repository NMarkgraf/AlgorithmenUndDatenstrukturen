'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Offener Hash / Open Hash

'''


from lists import Node, LinearList


class HashNode(Node):
    """Hashnode.

    Der Knoten in einem Hash hat nicht nur einen Schlüssel, sondern auch eine
    Infromtion(sspeicher). Daher wird die Klasse `Node` aus `lists`
    entsprechend erweitert.
    """

    def __init__(self):
        """Initialise HashNode.

        Eine HashNode ist eine Node (aus dem Paket `lists`) mit einer
        zusätzlichen Information (`_info`). Daher wird die Elternklasse
        initalisiert und das zusätzliche Attribute erzeugt.
        """
        super().__init__()
        self._info = None

# ============================================================================


class OpenHash(object):
    """Klasse OpenHash.

    Ein offener Hash ist ein Feld von linearen Listen. In welcher Liste eine
    gespeicherte Information steht oder stehen könnte wird aus dem Schlüssel
    mit Hilfe einer Hashfunktion ermittelt.
    """

    def __init__(self, heads=11, hashfkt=None):
        """Initialise OpenHash.

        Wir legen zunächst `heads` viele leere linare Listen an und speichern
        die Hashfunktion für die Suche.
        """
        # Private Attribute
        self.__heads = [None] * heads
        self.__hashfkt = hashfkt

        # Erzeuge `heads` viele Listenköpfe
        for i in range(0, heads):
            self.__heads[i] = LinearList(HashNode)

    def insertInHash(self, hsh, key, info):
        """Einfügen eines Schlüssels und einer Information im Hash.

        Wir fügen den Schlüssen `key` mit der Information `info` im
        Hash `hsh`ein.
        """
        # Füge Schlüssel ein ...
        t = self.__heads[hsh].insert(key)
        # ... und ergänze die Information
        t._info = info

    def insert(self, key, info):
        """Einfügen eines Schlüssels und einer Information.

        Wir erzeugen aus dem Schlüssel und der hinterlegten Hashfunktionen
        einen Aufruf von `insertInHash`.
        """
        return self.insertInHash(self.__hashfkt(key), key, info)

    def searchInHash(self, hsh, key):
        """Suche nach einem Schlüssen in einem Hash.

        Wir suchen den Schlüssel `key` im Hash `hsh` und liefert ggf
        die HashNode mit diesem Schlüssel.
        """
        return self.__heads[hsh].find(key)

    def search(self, key):
        """Suche nach einem Schlüssel.

        Wir suchen im ganzen Hash nach einer HashNode mit dem Schlüssel `key`.
        Dazu wird mit der Hashfunktion der Hash ausgesuche in dem das
        Objekt liegen könnte und mittels `seachInHash` danach gesucht.
        """
        return self.searchInHash(self.__hashfkt(key), key)

# ============================================================================


def hshfkt(x):
    """Hashfunktion.

    Beispiel für eine sehr einfache Hashfunktion.
    """
    t = 0
    for i in range(0, len(x)):
        t = (t + ord(x[i])) % 11
    return t

# ============================================================================


def printInfo(node):
    """Print node with its key and information.

    Gib den Knoten `node` aus, in dem man den Schlüssel und die Information
    angibt.
    """
    print(node._key+": ", node._info)

# ============================================================================


def main():
    """Hauptprogramm.

    Wir zählen das Vorkommen der Wörter in einem kleinen Text (`txt`).
    Dazu nutzen wir die Hashfunktion (`hshfkt`) und einen OpenHash mit
    11 Hashes.
    """
    openhash = OpenHash(11, hshfkt)

    txt = "Das ist ein kleiner Text. Er ist von mir geschrieben. "
    txt += "Dieser Test ist sinnfrei. Aber er dient einem guten Test!"

    for x in txt.replace(".", "").replace("!", "").split():
        t = openhash.search(x)
        if t:
            t._info += 1
        else:
            openhash.insert(x, 1)

    printInfo(openhash.search("ist"))
    printInfo(openhash.search("Test"))


if __name__ == "__main__":
    main()
