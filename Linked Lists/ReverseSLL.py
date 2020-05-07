'''
Reverse SLL
'''


# Iterative 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while (curr != None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode 
        return prev
            




# Recursive


def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)