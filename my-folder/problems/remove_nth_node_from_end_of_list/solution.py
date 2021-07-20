# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp_node =  head
        counter = 0
        while temp_node:                 
            counter = counter+1
            temp_node = temp_node.next
        if counter-n==0:
            head = head.next
            return head
        runner = head
        for i in range(counter-n):
            walker = runner
            runner = runner.next
        walker.next = runner.next
        runner.next = None
        return head  