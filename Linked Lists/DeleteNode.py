# Delete Node
# Delete Node in a linked list 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None #set next equal to none

class Solution:
    def deleteNode(self, node):
         next_node = node.next 
         if next_node: #check to see if next node exists
            node.val = node.next.val # set value of node to value of next node 
            node.next = node.next.next #set next pointer to next next pointer
         else:
             return False
    
