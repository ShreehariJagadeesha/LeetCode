# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head==None:
                return head
        
        while head and head.val==val:
            head=head.next
        
        current=head
        
        while current:
            
            if current.next and current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
                
        return head
            