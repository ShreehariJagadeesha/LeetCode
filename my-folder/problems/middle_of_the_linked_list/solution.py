# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        counter=0
        
        while current!=None:
            counter=counter+1
            current=current.next
            
        middlenodeindex=0
        
        if counter%2==0:
            middlenodeindex=(counter/2)+1
            print(middlenodeindex)
            
        else:
            middlenodeindex=int((counter/2)+1)
            print(middlenodeindex)
            
        for i in range(0,middlenodeindex-1):
            head=head.next
            
        return head
        