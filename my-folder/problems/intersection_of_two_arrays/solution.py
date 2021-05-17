import numpy as np

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0,len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i]==nums2[j]:
                    ans.append(nums1[i])
                    
#         for k in range(0,len(ans)):
#             if ans[k]==ans[k+1]:
#                 ans.pop(k+1)
                
        myFinalList = np.unique(ans).tolist()
        return myFinalList
                
        