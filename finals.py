import time
import random
import os
import math

class Stack(object):

   def __init__(self):
      self.items=[]
      return

   def push(self, val):
      self.items.append(val)
      return(self.items)

   def pop(self):
      self.items.pop()
      return(self.items)

   def getSize(self):
      size=len(self.items)
      print(size)
      return(size)

   def top(self):
      top=self.items[-1]
      print(top)
      return

   def display(self):
      print()
      print(self.items)
      print()
      return

def main():

   chi.push(1995)
   chi.display()
   print()
   chi.getSize()
   chi.top()
   chi.push(420)
   chi.push(2017)
   chi.display()
   chi.getSize()
   chi.top()
   chi.pop()
   print()
   chi.getSize()
   chi.top()
   print()
   
   


chi=Stack()
main()
