# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        one, two = "", ""
        while l1 or l2:
            if l1:
                one += str(l1.val)
                l1 = l1.next
            if not l1: one += str(0)
            if l2: 
                two += str(l2.val)
                l2 = l2.next
            if not l2: two += str(0)
        print(one)
        print(two)

        sm = int(one[::-1]) + int(two[::-1])
        print(sm)
        sm = [int(i) for i in str(sm)]
        print(sm)
        dummy = ListNode()
        cur = dummy
        for i in reversed(sm):
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next