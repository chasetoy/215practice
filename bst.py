class TreeNode(object):

   def __init__(self,key,moab,lft=None,rgt=None,item=None):
      self.ky=ky
      self.moab=moab
      self.lftChild=lft
      self.rgtChild=rgt
      self.item=item

   def getrgtLink(self):
      return self.rgtChild

   def getlftLink(self):
      return self.lftChild

   def getItem(self):
      return self.item

   def makeItem(self, newItem):
      self.item=newItem
      return

   def setlftLink(self, newLink):
      self.lftLink=newLink
      return

   def setrgtLink(self, newLink):
      self.rgtLink=newLink
      return

   def makeShit(self,ky,moab,lfc,rfc):
      self.key=ky
      self.moab=moad
      self.lftChild=lfc
      self.rgtChild=rfc
      if self.getlftLink():
         self.lftChild.item=self
      if self.getrgtLink():
         self.rgtChild.item=self

class BST(object):

   def __init__(self):
      self.root=None

   def set(self,ky,val):
      if self.root:
         self._set(ky,val,self.root)
      else:
         self.root=TreeNode(ky,val)

   def _set(self,ky,val,currNode):
      if ky < currNode.ky:
         if currNode.getlftLink():
            self._set(ky,val,currNode.lftChild)
         else:
            currNode.lftChild=TreeNode(ky,val,item=currNode)
      else:
         if currNode.getrgtLink():
            self._set(ky,val,currNode.rgtChild)
         else:
            currNode.rgtChild=TreeNode(ky,val,item=currNode)

   def __etitem__(self,r,z):
      self.set(r,z)

   def get(self,ky):
      if self.root:
         cat=self._get(ky,self.root)
         if cat:
            return cat.moab
         else:
            return None
      else:
         return None

   
