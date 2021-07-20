# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        dummy=head
        first=None
        second=None
        head1=None
        head2=None
        while dummy:
            if dummy.val<x and first==None:
                head1=dummy
                first=dummy
            elif dummy.val<x:
                first.next=dummy
                first=first.next
            elif dummy.val>=x and second==None:
                head2=dummy
                second=dummy
            elif dummy.val>=x:
                second.next=dummy
                second=second.next
            dummy=dummy.next
        if head1==None or head2==None:
            return head
        first.next=head2
        second.next=None
        return head1
