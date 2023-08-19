class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        ans=[]
        freq=dict()
        
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
        print(freq)

        for key,val in freq.items():
            if len(ans)<k:
                heapq.heappush(ans,[val,key])
            else:
                heapq.heappushpop(ans,[val,key])
        print(ans)
                
        return [key for value,key in ans]