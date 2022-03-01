class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N=len(s)
        output=0
        
        for a in range(N):
            i,j=a,a
            while 0<=i<N and 0<=j<N and s[i]==s[j]:
                output+=1
                i-=1
                j+=1
            i,j=a,a+1
            while 0<=i<N and 0<=j<N and s[i]==s[j]:
                output+=1
                i-=1
                j+=1
        return output