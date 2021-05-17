class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(temp==rev):
            return bool(True)
        else:
            return bool(False)
        