class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output=[]
        M=len(p)
        N=len(s)
        
        CounterS=Counter(p)
        CounterW=Counter(s[:M-1])
        for i in range(M-1,N):
            string_index=i-(M-1)
            CounterW[s[i]]=CounterW[s[i]]+1
            if CounterW==CounterS:
                output.append(string_index)
            CounterW[s[string_index]]=CounterW[s[string_index]]-1
            if CounterW[s[string_index]]==0:
                CounterW.pop(s[string_index])
        return output