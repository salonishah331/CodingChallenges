'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        dummyhead = ListNode(0)
        currprev = dummyhead
        while l1 or l2 or remainder:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            total = v1 + v2 + remainder
            remainder = int (total / 10)
            total = int (total % 10) 
            node = ListNode(total, None)
            currprev.next = node
            currprev = currprev.next
        return dummyhead.next