'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempHead = ListNode(0, None)
        carry = 0
        x = 0
        y = 0
        curr = tempHead
        while l1 or l2 or carry:
            x = 0 
            y = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            
            addedNode = x + y + carry
            
            carry = addedNode // 10
            
            curr.next = ListNode(addedNode % 10)
            curr = curr.next
            
        if carry > 0:
            curr.next = ListNode(carry)
        
        return tempHead.next
