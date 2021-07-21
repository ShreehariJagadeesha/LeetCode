class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return (lambda x : [i[0] for i in x])(Counter(nums).most_common(k))