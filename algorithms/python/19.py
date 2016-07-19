# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n):
            second = second.next
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
        
