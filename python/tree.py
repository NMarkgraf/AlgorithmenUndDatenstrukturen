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

  def __str__(self):
      return str(self._key)

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
    while x is not self._sentinal:
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
    if key < p._key:
      p._left = x
    else:
      p._right = x

  def search(self, key):
    x = self._head._right

    self._sentinal._key = key

    while (key != x._key):
      if (key < x._key):
        x = x._left
      else:
        x = x._right
    return x._info
    
  def inorderRecursiv(self, node):
    if node is not self._sentinal:
      self.inorderRecursiv(node._left)
      self.printnode(node)
      self.inorderRecursiv(node._right)

  def preorderRecursiv(self, node):
    if node is not self._sentinal:
      self.printnode(node)
      self.preorderRecursiv(node._left)
      self.preorderRecursiv(node._right)

  def postorderRecursiv(self, node):
    if node is not self._sentinal:
      self.postorderRecursiv(node._left)
      self.postorderRecursiv(node._right)
      self.printnode(node)

  def preorderIterativ(self):
      stack = []  # Wir benutzen einmal den Python eigenen Stack, eine Liste. ;-)
      
      stack.append(self._head._right)
      
      while stack:
          n = stack.pop()
          self.printnode(n)
          if n._right is not self._sentinal:
              stack.append(n._right)
          if n._left is not self._sentinal:
              stack.append(n._left)


  def inorderIterativ(self):
      stack = []  # Wir benutzen einmal den Python eigenen Stack, eine Liste. ;-)
      
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

  def postorderIterativ(self):
      stack = []  # Wir benutzen einmal den Python eigenen Stack, eine Liste. ;-)
      
      n = self._head._right

      done = False
      
      while not done:
        
        while (n is not self._sentinal):
            if n._right is not self._sentinal:
                stack.append(n._right)
            stack.append(n)
            n = n._left
        
        n = stack.pop()
        
        if n._right is not self._sentinal and stack and stack[-1] is n._right:
            stack.pop()
            stack.append(n)
            n = n._right
        else:
            self.printnode(n)
            n = self._sentinal
        if not stack:
            done = True


  def levelorderIterativ(self):
      from collections import deque
      queue = deque([])  # Wir benutzen einmal den Python eigene Queue, eine deque(Liste). ;-)
      
      queue.append(self._head._right)
      
      while queue:
          n = queue.popleft()
          self.printnode(n)
          if n._left is not self._sentinal:
              queue.append(n._left)
          if n._right is not self._sentinal:
              queue.append(n._right)
          

  def printnode(self, node):
    print("["+str(node._key)+": "+str(node._info), end="] " ,flush=True)
    


def main():
  tree = Tree()
  tree.insert(20, "20")
  tree.insert(10, "10")
  tree.insert(5, "5")
  tree.insert(15, "15")
  tree.insert(30, "30")
  tree.insert(25, "25")
  tree.insert(35, "35")
  '''
  Der aufgebaute Baum:
  
                 [20]
                 
        [10]               [30]
        
    [ 5]    [15]       [25]    [35]
  
  '''

  print("\nRekursive Traversierung:")
  print("Preorder:")
  tree.preorderRecursiv(tree._head._right)
  print("\nInorder:")
  tree.inorderRecursiv(tree._head._right)
  print("\nPostorder:")
  tree.postorderRecursiv(tree._head._right)

  print("\n\nIterative Traversierung:")
  print("Preorder:")
  tree.preorderIterativ()
  print("\nInorder:")
  tree.inorderIterativ()
  print("\nPostorder:")
  tree.postorderIterativ()
  print("\nLevelorder:")
  tree.levelorderIterativ()

  print("")

def test():
    from random import randint
    
    tree = Tree()
    n = 1000
    
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
