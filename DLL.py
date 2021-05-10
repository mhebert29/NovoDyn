#!/usr/bin/env python3
import sys
import os
import json
import pathlib
from collections import deque

# Node of DLL
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

# Code for inserting data to tree
  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.prev is None:
          self.prev = Node(data)
        else:
          self.prev.insert(data)

      elif data > self.data:
        if self.next is None:
          self.next = Node(data)
        else:
          self.next.insert(data)
    else:
      self.data = data

# Print tree
  def PrintTree(self):
    if self.prev:
      self.prev.PrintTree()
    print( self.data),
    if self.next:
      self.next.PrintTree()

########################################
# Iterative function to perform postorder traversal on the tree
def postorderIterative(root):

	# create an empty stack and push the root node
    output = []
    stack = deque()
    stack.append(root)

	# create another stack to store postorder traversal
    out = deque()

	# loop till stack is empty
    while stack:

		# pop a node from the stack and push the data into the output stack
        curr = stack.pop()
        out.append(curr.data)

		# push the left and right child of the popped node into the stack
        if curr.prev:
            stack.append(curr.prev)

        if curr.next:
            stack.append(curr.next)

	# print postorder traversal
    while out:
        output.append(out.pop())
		#print(out.pop(), end=' ')
    return output
#############################################

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  #Create/ return new node
  def getNode(self, data):
    return Node(data)

  def sortedInsert(self, data):
    new_node = self.getNode(data)

    # If list is empty
    if self.head is None:
      self.head = new_node
    # If to be inserted at beginning
    elif self.head.data >= new_node.data:
      new_node.next = self.head
      new_node.next.prev = new_node
      self.head = new_node
    else:
      current = self.head

      while((current.next is not None) and (current.next.data < new_node.data)):
        current = current.next

      new_node.next = current.next

      if current.next is not None:
        new_node.next.prev = new_node

      current.next = new_node
      new_node.prev = current


  # Function to print doubly linked list
 # def printList(self):
  #  node = self.head
   # while node:
    #  print(str(node.data), end = " ")
     # node = node.next

###################################################
def makeOutput(llist):
  output = []
  root = Node(0)
  DLL = DoublyLinkedList()

# Sort inputs
  for key in llist:
    DLL.sortedInsert(key)

# Insert sorted inputs into tree
  for key, value in llist.items():
      root.insert(key)

# Iterate tree in a portOrder form and add recpective
# value of key to output list
  for i in postorderIterative(root):
      output.append(llist[i])

  return output

