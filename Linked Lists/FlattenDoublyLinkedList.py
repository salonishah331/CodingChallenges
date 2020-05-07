'''
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, 
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure,
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
'''


# Recursive Solution

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flattenHelper(head)
        return head
        
        
        
        
    def flattenHelper(self, node):
        while node:
            q = node.next
            if not q:
                tail = node
            if node.child:
                node.next = node.child
                node.child.prev = node
                t = self.flattenHelper(node.child)
                if q:
                    q.prev = t
                t.next = q
                node.child = None
            node = node.next
        return tail
                
# Iterative Solution


