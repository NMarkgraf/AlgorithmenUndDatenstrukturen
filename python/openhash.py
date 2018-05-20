'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Offener Hash. / Open Hash

'''


from lists import Node, LinearList


class HashNode(Node):

    def __init__(self):
        super().__init__()
        self._info = None

class OpenHash(object):
    
    def __init__(self, heads=11, hashfkt=None):
        self.__heads = [None] * heads 
        self.__hashfkt = hashfkt
        for i in range(0, heads):
            self.__heads[i] = LinearList(HashNode)
        
    def insertInHash(self, hsh, key, info):
        t = self.__heads[hsh].insert(key)
        t._info = info
        
    def insert(self, key, info):
        return self.insertInHash(self.__hashfkt(key), key, info)
        
    def searchInHash(self, hsh, key):
        return self.__heads[hsh].find(key)
        
    def search(self, key):
        return self.searchInHash(self.__hashfkt(key), key)
    

def hshfkt(x):
    t = 0
    for i in range(0, len(x)):
        t = (t + ord(x[i])) % 11
    return t


def printInfo(node):
    print(node._key+": ", node._info)


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
