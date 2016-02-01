# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        cur = head
        carry = 0
        while l1 != None or l2 != None or carry != 0 :
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            res += carry
            if res >9:
                res -= 10
                carry = 1
            else:
                carry = 0
            tmpNode = ListNode(res)
            cur.next = tmpNode
            cur = tmpNode
        return head.next
            
        
            
        
