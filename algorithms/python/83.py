# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        second = head.next if first != None else None
        while first and second:
            first_val = first.val
            second_val = second.val
            if first_val == second_val:
                if second.next == None:
                    first.next = None
                    break
                second = second.next
            else:
                first.next = second
                second = second.next
                first = first.next
        return head 

        
