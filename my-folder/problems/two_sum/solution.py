class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_dict={}
        for i, num in enumerate(nums):
            remaining = target-num
            if remaining in value_dict:
                return [value_dict[remaining],i]
            value_dict[num]=i
        return []