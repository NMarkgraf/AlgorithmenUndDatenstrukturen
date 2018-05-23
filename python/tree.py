'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Binärer Such-Baum

'''

# ============================================================================


class Node:
    """Tree Node.

    Ein einfacher Baum-Knoten. Er besteht aus einem Schlüssel `_key`, einem
    linken und einem rechten Kindknoten `_left` und `_right`, sowie einem
    Informationsspeicher `_info` in dem weitere Daten gespeichert werden
    können.
    """

    _key = None  # Schlüssel
    _left = None  # Linker Kindknoten
    _right = None  # Rechter Kindknoten
    _info = None  # Information(sspeicher)

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getInfo(self):
        return self._info

    def __lt__(self, a, b):
        return a._key < b.key

    def __le__(self, a, b):
        return a._key <= b.key

    def __eq__(self, a, b):
        return a._key == b._key

    def __gt__(self, a, b):
        return a._key > b.key

    def __ge__(self, a, b):
        return a._key >= b.key

    def __ne__(self, a, b):
        return a._key != b._key

    def __repr__(self):
        return "("+repr(self._key)+": "+repr(self._info)+")"

    def __str__(self):
        return "("+str(self._key)+": "+str(self._info)+")"

# ============================================================================


class Tree:
    """Binary tree.

    Ein binärer Baum mit Sentialtechnik.
    """

    _head = None  # Start Knoten, aber KEINE echteWurzel
    _sentinal = None  # Sentinal als Ersatz für ein `None`

    def __init__(self):
        """Initialise binary tree.

        Erzeuge einen neuen binären Baum.
        """
        self._head = Node()
        self._sentinal = Node()
        self._sentinal.key = -1
        self._sentinal._left = self._sentinal
        self._sentinal._right = self._sentinal
        self._head._right = self._sentinal
        self._head._key = -1

    def insert(self, key, info):
        """Insert a new node with key and infoself.

        Füge einen neinen Knoten mit Schlüssel (key) und Information (info)
        ein.
        """
        p = self._head
        x = self._head._right
        while x is not self._sentinal:
            p = x
            if (key < x._key):
                x = x._left
            else:
                x = x._right
        x = Node()
        x._key = key
        x._info = info
        x._left = self._sentinal
        x._right = self._sentinal
        if key < p._key:
            p._left = x
        else:
            p._right = x

    def __search(self, key):
        # Wir starten hinter derm Kopfknoten an der Wurzel
        x = self._head._right

        # Sentinaltechnik! Wir setzen den Sential auf den Suchwert!
        self._sentinal._key = key

        # Suchen bis der Suchwert gefunden wird.
        while (key != x._key):  # Dank Sentinaltechnik werden wir finden!
            if (key < x._key):
                x = x._left
            else:
                x = x._right
        return x

    def search(self, key):
        """Search in the tree.

        Suchen im Baum. Wir liefern `None` zurück, wenn wir der Schlüssel `key`
        nicht im Baum finden. Sonst wir Information`_info` zurückgeliefert.

        :param: key Suchschlüssel
        """
        x = self.__search(key)
        return x if x is not self._sentinal else None

    def preorderRecursive(self, node):
        """Traverse the tree in preorder recursive.

        Preorder Traversierung des Baumes mittels Rekursion.
        """
        if node is not self._sentinal:
            self.printnode(node)
            self.preorderRecursive(node._left)
            self.preorderRecursive(node._right)

    def inorderRecursive(self, node):
        """Traverse the tree inorder recursive.

        Inorder Traversierung des Baumes mittels Rekursion.
        """
        if node is not self._sentinal:
            self.inorderRecursive(node._left)
            self.printnode(node)
            self.inorderRecursive(node._right)

    def postorderRecursive(self, node):
        """Traverse the tree postorder recursive.

        Postorder Traversierung des Baumes mittels Rekursion.
        """
        if node is not self._sentinal:
            self.postorderRecursive(node._left)
            self.postorderRecursive(node._right)
            self.printnode(node)

    def preorderIterative(self):
        """Traverse the tree postorder iterative.

        Preorder Traversierung des Baumes mittels Iteration und eines Stacks.
        """
        stack = []  # Wir benutzen den Python eigenen Stack: eine Liste.

        stack.append(self._head._right)

        while stack:
            n = stack.pop()
            self.printnode(n)
            if n._right is not self._sentinal:
                stack.append(n._right)
            if n._left is not self._sentinal:
                stack.append(n._left)

    def inorderIterative(self):
        """Traverse tree inorder iterative.

        Inorder Traversierung des Baumes mittels Iteration und eines Stacks.
        """
        stack = []  # Wir benutzen den Python eigenen Stack: eine Liste.

        n = self._head._right

        while (n is not self._sentinal):
            stack.append(n)
            n = n._left

        while stack:
            n = stack.pop()
            self.printnode(n)
            n = n._right
            while (n is not self._sentinal):
                stack.append(n)
                n = n._left

    def postorderIterative(self):
        """Traverse tree postorder iterative.

        Postorder Traversierung des Baumes mittels Iteration und eines Stacks.
        """
        stack = []  # Wir benutzen den Python eigenen Stack: eine Liste.

        n = self._head._right

        done = False

        while not done:

            while (n is not self._sentinal):
                if n._right is not self._sentinal:
                    stack.append(n._right)
                stack.append(n)
                n = n._left

            n = stack.pop()

            if (n._right is not self._sentinal
               and stack
               and stack[-1] is n._right):
                stack.pop()
                stack.append(n)
                n = n._right
            else:
                self.printnode(n)
                n = self._sentinal
            if not stack:
                done = True

    def levelorderIterative(self):
        """Traverse tree levelorder iterative.

        Inorder Traversierung des Baumes mittels Iteration und eines Stacks.
        """
        from collections import deque
        queue = deque([])  # Wir benutzen die Python eigene Queue, eine deque.

        queue.append(self._head._right)

        while queue:
            n = queue.popleft()
            self.printnode(n)
            if n._left is not self._sentinal:
                queue.append(n._left)
            if n._right is not self._sentinal:
                queue.append(n._right)

    def printnode(self, node):
        """Print node information.

        Gib die aktuelle Node (Schlüssel und Infromation) aus.
        """
        print(str(node), end=" ", flush=True)

    def __deleteLeaf(self, leaf):
        """Deleate leaf.

        Lösche das Blatt/Knoten in dem man es durch das linke Kind ersetzt.
        """
        leaf = leaf._left
        return leaf

    def __deleteNodeWithLeaf(self, node):
        """Delete node with leaf.

        Lösche einen Knoten mit einem Blatt als Kind.
        """
        t = node
        node = node._right
        node._left = t._left
        return node

    def __deleteBySubstitution(self, node, dnode):
        """Delete node by substitution.

        Lösche den Knoten `dnote` durch Substituion.
        """
        n = node._right
        while n._left._left is not self._sentinal:
            n = n._left
        node = n._left
        n._left = node._right
        node._left = dnode._left
        node._right = dnode._right
        return node

    def delete(self, key):
        """Delete node by key.

        Lösche einen Knoten mit dem angegebenen Schlüssel.

        Es gibt dazu drei Fälle zu unterscheiden:
        1. Der zu löschende Knoten ist ein Blatt
        """
        # Beginne an der Wurzel
        p = self._head  # Knoten über der Wurzel
        n = self._head._right  # Der Wurzelknoten
        # Bereite eine Suche vor (mit Sentinaltechnik)
        self._sentinal._key = key
        # Suche nach dem Knoten, welche gelöscht werden soll
        while key != n._key:
            p = n  # Knoten aus dem ein Kind gelöscht wird
            n = n._left if (key < n._key) else n._right
        t = n  # t ist nun der zu löschende Knoten

        if t._right is self._sentinal:
            # Lösche einen Knoten, der keine rechten Kindknoten mehr hat.
            n = self.__deleteLeaf(n)
        else:
            # Es gibt einen rechten Kindknoten ...
            if t._right._left is self._sentinal:
                # ... aber der hat keinen linken Kindknoten!
                n = self.__deleteNodeWithLeaf(n)
            else:
                # ... und der hat einen linken Kindknoten!
                n = self.__deleteBySubstitution(n, t)
        if key < p._key:
            p._left = n
        else:
            p._right = n

    
def main():
    """Hauptprogramm.

    Wir bauen einen kleinen Baum auf und traversieren diesen mit den
    verschiedenen implementierten Methoden.

    Der folgende Baum wird zunächst aufgebaut:

                 [20]

        [10]               [30]

    [ 5]    [15]       [25]    [35]

    """
    tree = Tree()
    tree.insert(20, "20")
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(30, "30")
    tree.insert(25, "25")
    tree.insert(35, "35")

    print("\nRekursive Traversierung:")
    print("Preorder:")
    tree.preorderRecursive(tree._head._right)
    print("\nInorder:")
    tree.inorderRecursive(tree._head._right)
    print("\nPostorder:")
    tree.postorderRecursive(tree._head._right)

    print("\n\nIterative Traversierung:")
    print("Preorder:")
    tree.preorderIterative()
    print("\nInorder:")
    tree.inorderIterative()
    print("\nPostorder:")
    tree.postorderIterative()
    print("\nLevelorder:")
    tree.levelorderIterative()

    print("")


def testZwei():
    tree = Tree()
    tree.insert(20, "20")
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(30, "30")
    tree.insert(25, "25")
    tree.insert(35, "35")

    tree.inorderIterative()
    print("")
    tree.preorderIterative()

    print("\nLösche das Blatt 35:")
    tree.delete(35)
    tree.inorderIterative()
    print("")
    tree.preorderIterative()
    print("")
    print("\nLösche das Blatt 10:")
    tree.delete(10)
    tree.inorderIterative()
    print("")
    tree.preorderIterative()
    print("")
    print("\nLösche das Blatt 20:")
    tree.delete(20)
    tree.inorderIterative()
    print("")
    tree.preorderIterative()
    print("")


def test():
    from random import randint

    tree = Tree()
    n = 10

    list = [0] * n
    for i in range(0, n):
        list[i] = randint(0, n**2)

    for value in list:
        tree.insert(value, str(value))

    tree.inorderIterativ()
    print("")
    tree.inorderRecursiv(tree._head._right)
    print("")



if __name__ == "__main__":
    main()
    # test()
    # testZwei()
