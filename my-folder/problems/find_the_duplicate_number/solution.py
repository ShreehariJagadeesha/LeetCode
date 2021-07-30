class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for i in nums:
            if not i in hashmap:
                hashmap[i] = True
            else:
                return i