'''
Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Listen. - Pyhton hat eigentlich eine optimierte Listenverwaltung. 

Da es aber um die grundlegenden Algorithmen geht, 
machen wir davon weitgehend keinen Gebrauch!

*Node* ist unsere Klasse für unsere Datenknoten

*LinearList* ist unsere Basisklasse für die Lineare Liste, von Ihr werden

*Stack* für einen Stack / Stapelspeicher und

*Queue* für eine Schlange abgeleitet.


'''

from abc import ABC, abstractmethod

class Node:
    
  _key = None
  _next = None

  def __init__(self):
    self._key = None
    self._next = None

  def __repr__(self):
      return repr(self._key)
      
  def __str__(self):
      return str(self._key)


class AbstractLinearList(ABC):

  _head = None
  _tail = None

  @abstractmethod
  def insertafter(self, node, value):
      ''' insert new value after node
      '''
      pass
  
  @abstractmethod
  def deletenext(self, node):
      ''' delete next node
      '''
      pass

  @abstractmethod
  def search(self, node, value):
      ''' search for value starting at node
      '''
      pass

  @abstractmethod
  def isempty(self):
      ''' is list empty?
      '''
      pass
  
# -----------------------------------------------------------------------
class LinearList(AbstractLinearList):
    
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head._next = self._tail
        self._head._key = -1
        self._tail._key = -1
        self._tail._next = self._tail
    
    def __repr__(self):
        t = self._head._next
        rs = ""
        while (t._next != t):
            rs += repr(t) + " "
            t = t._next
          
        return(rs)
      
    def __str__(self):
        t = self._head._next
        rs = "["
        while (t._next != t):
            rs += str(t) + ", "
            t = t._next 
          
        rs += "]"
        return(rs)
    
    def insertafter(self, node, value):
      newNode = Node()
      newNode._key = value
      newNode._next = node._next
      node._next = newNode
      return newNode
      
    def deletenext(self, node):
      t = node._next
      v = node._next._key
      node._next = node._next._next
      if (t != self._tail):
          del(t)
      return v
      
    def search(self, node, value):
        ''' search
           
           Suche mit Sentinaltechnik
        '''
        self._tail._key = value
        while (node._key != value):
            node = node._next
        return node
    
    def isempty(self):
        return self._head._next == self._tail
    
    def istail(self, node):
        return node._next == node
        
    def isinlist(self, value):
        node = self.search(self._head, value)
        return not self.istail(node)
 
# -----------------------------------------------------------------------
class SortedLinearList(LinearList):
    ''' Implementiert eine sortierte linearen Liste
    '''
    
    def search(self, node, value):
        self._tail._key = value
        while (node._next._key < value):
            node = node._next
        return node
    
    def insert(self, value):
        n = self.search(self._head, value)
        self.insertafter(n, value)


# -----------------------------------------------------------------------
class Stack(LinearList):
    ''' Implementiert einen Sack mit Hilfe einer linearen Liste
    '''
    
    def push(self, value):
        self.insertafter(self._head, value)
        
    def pop(self):
        return self.deletenext(self._head)


# -----------------------------------------------------------------------
class Queue(LinearList):
    ''' Implementiert eine Queue (Schlange) mit Hilfe einer linearen Liste
    '''
    
    def get(self):
        return self.deletenext(self._head)
        
    def put(self, value):
        t = self._head
        while (t._next != self._tail):
            t = t._next
        self.insertafter(t, value)
 
 
# -----------------------------------------------------------------------
class Ring(LinearList):
  ''' Implementiert einen Ring mit Hilfe einer linearen Liste
  '''
  
  def __init__(self):
    super().__init__()
    self._head._next = self._head
        
  def __repr__(self):
      rs = "("
      n = self._head._next
      while n._next != self._head._next:
          rs += repr(n) + " "
          n = n._next
      rs += repr(n) + ")"
      return rs

  def __str__(self):
      rs = "("
      n = self._head._next
      while n._next != self._head._next:
          rs += str(n) + ", "
          n = n._next
      rs += str(n) + ")"
      return rs

  def isempty(self):
    return self._head._next == self._head

  def insert(self, value):
    tail = self._head._next
    while tail._next != self._head._next:
        tail = tail._next
    newnode = self.insertafter(tail, value)
    if newnode._next == self._head:
        newnode._next = newnode
        
  def searchnext(self, node, value):
    while (node._next._key != value):
        node = node._next
        if node._next == self._head._next:
            break
    return node

  def delete(self, value):
      node = self.searchnext(self._head, value)
      if node._next != self._head._next:
          self.deletenext(node)

  def getnext(self, node):
      return node._next

# ===========================================================================
def main():
    # -----------------------------------------------------------------------
    print("Lineare Liste:")
    list = LinearList()

    print(list) 
    list.insertafter(list._head, 1)
    print(list) 
    nn = list.insertafter(list._head, 2)
    print(list)    
    list.insertafter(nn, 4)
    print(list)    
    nn = list.insertafter(nn, 42)
    print(list)    
    list.insertafter(nn, 4711)
    print(list)

    # -----------------------------------------------------------------------
    print("Sortierte lineare Liste:")
    list = SortedLinearList()
    print(list) 
    list.insert(4711)
    print(list)
    list.insert(1)
    print(list) 
    list.insert(4)
    print(list)    
    list.insert(2)
    print(list)    
    list.insert(42)
    print(list)    
    

    # -----------------------------------------------------------------------
    print("Stack:")
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    while not stack.isempty():
        print(stack.pop())
    
    # -----------------------------------------------------------------------
    print("Queue:")
    queue = Queue()

    queue.put(1)
    queue.put(2)
    queue.put(3)

    while not queue.isempty():
        print(queue.get())

    # -----------------------------------------------------------------------
    print("Ring:")
    ring = Ring()
    
    ring.insert(1)
    ring.insert(2)
    ring.insert(3)
    ring.insert(4)

    print(ring)

    ring.delete(2)
    
    print("- - - -")

    print(ring)

if __name__ == "__main__":
    main()