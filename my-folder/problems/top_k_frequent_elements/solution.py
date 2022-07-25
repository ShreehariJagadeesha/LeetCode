class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        freq=dict()
        
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
                
        for key,val in freq.items():
            if len(ans)<k:
                heapq.heappush(ans,[val,key])
            else:
                heapq.heappushpop(ans,[val,key])
                
        return [key for value,key in ans]