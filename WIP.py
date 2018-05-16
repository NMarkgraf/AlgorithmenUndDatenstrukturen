# -----------------------------------------------------------------------
class NewNode(Node):
    
    self._value = None


class LinearListNewNode(LinearList):
    
    def insertafter(self, node, key, value):
      newNode = NewNode()
      newNode._key = key
      newNode._value = value
      newNode._next = node._next
      node._next = newNode
      return newNode


class OpenHeap:
  ''' Implementiert einen offenen Heap  mit Hilfe von linearen Listen
  '''

  def __init__(self, headnumbers):
      self.M = headnumerbs
      self.heads = [LineareListNewNode()] * self.M
      
  def hash(self, k):
      h = 0
      for letter in k:
          h += (int(letter) - int("a")) % self.M
      return h % self.M

  def insert(self, key, hsh, value):
      self.heads[hsh].insertafter(self.heads[hsh], key, value)
      
  def findinhash(self, key, hsh):
      t = self.heads[hsh]
      t._tail._key = k
      while (t._key != key)
        t = t._next
      return t
