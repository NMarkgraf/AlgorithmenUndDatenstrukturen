'''
Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Binärer Such-Baum

'''

class Node:

  _key = None
  _left = None
  _right = None
  _info = None

  def getLeft(self):
    return self._left

  def getRight(self):
    return self._right


class Tree:

  _head = None
  _sentinal = None
  
  def __init__(self):
    self._head = Node()
    self._sentinal = Node()
    self._sentinal.key = -1
    self._sentinal._left = self._sentinal
    self._sentinal._right = self._sentinal
    self._head._right = self._sentinal
    self._head._key = -1
    
  def insert(self, key, info):
    p = self._head
    x = self._head._right
    while (x != self._sentinal):
      p = x;
      if (key < x._key):
        x = x._left
      else:
        x = x._right
    x = Node()
    x._key = key
    x._info = info
    x._left = self._sentinal
    x._right = self._sentinal
    if (key < p._key):
      p._left = x
    else:
      p._right = x

  def search(self, key):
    x = self._head._right

    self._sentinal._key = key

    while ( key != x._key):
      if (key < x._key):
        x = x._left
      else:
        x = x._right
    return x._info

    
  def inorderRecursiv(self, node):
    if node != self._sentinal:
      self.inorderRecursiv(node._left)
      self.printnode(node)
      self.inorderRecursiv(node._right)


  def preorderRecursiv(self, node):
    if node != self._sentinal:
      self.printnode(node)
      self.preorderRecursiv(node._left)
      self.preorderRecursiv(node._right)

  def postorderRecursiv(self, node):
    if node != self._sentinal:
      self.postorderRecursiv(node._left)
      self.postorderRecursiv(node._right)
      self.printnode(node)

      
  def printnode(self, node):
    print("["+str(node._key)+": "+str(node._info), end="] " ,flush=True)
    

def main():
  tree = Tree()
  tree.insert(20, "20")
  tree.insert(10, "10")
  tree.insert(5, "5")
  tree.insert(15, "15")

  print("Preorder:")
  tree.preorderRecursiv(tree._head._right)
  print("\nInorder:")
  tree.inorderRecursiv(tree._head._right)
  print("\nPostorder:")
  tree.postorderRecursiv(tree._head._right)

if __name__ == "__main__":
    main()
