# Reverse Linked List 
# Write a function to reverse a linked list 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head)
        curr = head 
        prev = None 
        next_node = None

        while curr is not None: #till the end of the list
            next_node = curr.next #set pointer to the node after curr 
            curr.next = prev #reverse the next pointer
            prev = curr #set prev node to current node
            curr = next_node #set current node to next node
            
    
          
        return prev
        
