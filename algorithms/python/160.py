# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        lengthA = 1
        lengthB = 1
        while pA.next:
            pA = pA.next
            lengthA += 1
        while pB.next:
            pB = pB.next
            lengthB += 1
        if pA != pB:
            return None
        pA = headA
        pB = headB
        diff = lengthA - lengthB
        # lengthA > lengthB
        if diff > 0:
            while diff:
                pA = pA.next
                diff -= 1
        elif diff < 0:
            while diff:
                pB = pB.next
                diff += 1
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA

