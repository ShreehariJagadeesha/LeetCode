class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l=l-1
                r=r+1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            test=helper(i,i)
            if len(test)>len(res):res=test
            test=helper(i,i+1)
            if len(test)>len(res):res=test
                
        return res
                