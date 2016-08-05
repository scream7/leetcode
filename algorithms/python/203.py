# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head and head.val == val:
            head = head.next
        prev, run = None, head
        while run:
            if run.val == val:
                prev.next = run.next
            else:
                prev = run
            run = run.next
        return head
 
