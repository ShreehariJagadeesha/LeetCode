class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=Counter(nums)
        return (i for i in a if a[i]==2)