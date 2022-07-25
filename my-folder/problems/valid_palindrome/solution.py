class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def alphaNum(self,c):
            return (ord('A')<= ord(c)<=ord('Z') or ord('a')<= ord(c)<=ord('z') or ord('0')<= ord(c)<=ord('9') )        

        l,r=0,len(s)-1
        
        while l<r:
            while l<r and not alphaNum(self,s[l]):
                l=l+1
            while l<r and not alphaNum(self,s[r]):
                r=r-1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True
        

            
