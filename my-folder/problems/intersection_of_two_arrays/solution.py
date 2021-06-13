class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
#         temp=[]
#         i=0
#         j=0
#         while i < len(nums1):
#             while j < len(nums2):
#                 if nums1[i]==nums2[j]:
#                     temp.append(nums1[i])
#                 j=j+1
#             j=0
#             i=i+1
                    
#         indivisualset=set(temp)
#         finallist=list(indivisualset)
        
#         return finallist 
        
        set_nums1=set(nums1)
        set_nums2=set(nums2)
        return set_nums1.intersection(set_nums2)