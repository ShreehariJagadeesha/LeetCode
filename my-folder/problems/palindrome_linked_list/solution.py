# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=[]
        if head is None:
            return None
        while head !=None:
            if head.val == 0:
                temp.append(0)
            else:
                temp.append(head.val)
                
            head=head.next
        
        temp_1=temp[::-1]
        
        
        if temp_1==temp:
            return True
        else:
            return False