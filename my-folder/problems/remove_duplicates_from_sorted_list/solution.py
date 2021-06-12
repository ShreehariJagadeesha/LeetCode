# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        
        while a:
            b = a.next
            while b and a.val==b.val:
                b = b.next
            a.next = b
            a = a.next
        return head
        