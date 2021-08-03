# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
	        return head
        temp=head
        c=0
        while temp!=None:
	        c+=1
	        temp=temp.next
        for _ in range(k%c):
            prev=None
            curr=head
            while curr.next!=None:
                prev=curr
                curr=curr.next
            curr.next=head
            head=curr
            prev.next=None
        return head