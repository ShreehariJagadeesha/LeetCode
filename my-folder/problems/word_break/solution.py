class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d=set(wordDict)
        n=len(s)
        
        dp=[False for _ in range(n+1)]
        dp[0]=True
        for start in range(n):
            if not dp[start]:continue
            for end in range(start+1,n+1):
                if s[start:end] in d: dp[end]=True
        
        return dp[-1]
    