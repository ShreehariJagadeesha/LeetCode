# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy=head
        res=dummy.next   
        while True:
            pointer1=dummy.next  
            pointer2=dummy.next.next    
            pointer1.next=dummy   
            if not pointer2 or not pointer2.next:
                dummy.next=pointer2    
                break
            pointer1.next.next=pointer2.next
            dummy=pointer2
    
        return res