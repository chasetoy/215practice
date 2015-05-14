class TreNode(object):

   def __init__(self, item=None, leftLink=None, rightLink=None):
      self.item=item
      self.leftLink=leftLink
      self.rightLink=rightLink
      return

   def getItem(self):
      return self.item

   def getLeftLink(self):
      return self.leftLink

   def getrightLink(self):
      return self.rightLink

   def setItem(self, newItem):
      self.item=newItem
      return

   def setLeftLink(self, newLink):
      self.leftLink=newItem
      return

   def setRightLink(self, newLink):
      self.rightLink=newLink
      return

   def _testit(self):
      print("testit called")
      return


def BST(object):

   def __init__(self):
      self.root=None
      return

   def insert(self, item):
      self.root=self._insert(self.root, newItem)
      return

   def insert(self, item):
      if root is None:
         return TreeNode(item)

      if item == root.item:
         raise ValueError("inserting duplicate item bro!")

      if item < root.item:
         self._insert(root.leftLink, item)
      else:
         self._insert(root.rightLink, item)

      return root

   def find(self, target):
      return self._find(self.root, target)

   def _find(self, root, target):
      if root is None:
         return None

      if target == root.item:
         return root.item

      if target > root.item:
         return self._find(root.rightLink, target)
      else:
         return self._find(root.leftLink, target)


   def show(self):
      self._show(self, root, 0)
      return

   def _show(self,root,level):
      if root != None:
         print(" "*level, root.item)
         self._show(root.leftLink, level+1)
         self._show(rootrightLink, level+1)
      return

   
