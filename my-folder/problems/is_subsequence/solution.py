class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        for c in t:
            if i==len(s): return True
            if c==s[i]:
                i=i+1
        return i==len(s)
            