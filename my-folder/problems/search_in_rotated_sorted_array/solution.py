class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N=len(nums)
        l=0
        r=N-1
        while (l<r):
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        
        pivot=l
        l=0
        r=N-1
        while (l<=r):
            mid=(l+r)//2
            mid2=(pivot+mid)%N
            if nums[mid2]==target:
                return mid2
            elif nums[mid2]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
                