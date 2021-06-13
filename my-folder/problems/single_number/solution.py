class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        least_common = collections.Counter(nums).most_common()[-1]
        return least_common[0]