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
        super().__init__()
        self._info = None

# ============================================================================


class OpenHash(object):
    
    def __init__(self, heads=11, hashfkt=None):
        # Private Attribute
        self.__heads = [None] * heads 
        self.__hashfkt = hashfkt
        
        # Erzeuge `heads` viele Listenköpfe
        for i in range(0, heads):
            self.__heads[i] = LinearList(HashNode)
        
    def insertInHash(self, hsh, key, info):
        # Füge Schlüssel ein ...
        t = self.__heads[hsh].insert(key)
        # ... und ergänze die Information
        t._info = info
        
    def insert(self, key, info):
        return self.insertInHash(self.__hashfkt(key), key, info)
        
    def searchInHash(self, hsh, key):
        return self.__heads[hsh].find(key)
        
    def search(self, key):
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
    
    Gib den Knoten `node` aus, in dem man den Schlüssel und die Information angibt.
    """
    print(node._key+": ", node._info)

# ============================================================================


def main():
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
