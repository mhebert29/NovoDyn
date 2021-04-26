#!/usr/bin/env python3
# Python 3 version of CC04 Sorted Doubly Linked List
# Replace numbers in main with data images
#   Potentially use their md5sum, mod, or pre-assigned int to establish
#   numerical value flags
#

# Node of DLL
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

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

    # Locate node after which current node is to be inserted
    # We are thinking of modfying this while loop to incorporate image
    #   data flags so they may be ordered by the dentist before hand with
    #   a simply gui that'll take in minimal data for an optimized and targeted
    #   sorting of data.
      while((current.next is not None) and (current.next.data < new_node.data)):
        current = current.next

      new_node.next = current.next

      if current.next is not None:
        new_node.next.prev = new_node

      current.next = new_node
      new_node.prev = current


  # Function to print doubly linked list
  def printList(self):
    node = self.head
    while node:
      print(str(node.data), end = " ")
      node = node.next

  #Driver code
if __name__ == '__main__':
  llist = DoublyLinkedList()
  llist.sortedInsert(8)
  llist.sortedInsert(4)
  llist.sortedInsert(20)
  llist.sortedInsert(17)

  print("Created Doubly Linked List")
  llist.printList()
  print("\n")

# This Code is contributed by Siddhartha Pramanik
