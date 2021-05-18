class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
                
        d = {'I':1,
         'V':5,
         'X':10,
         'L':50,
         'C':100,
         'D':500,
         'M':1000}
        
        n_prev = ans = d[s[0]]
        for char in s[1:]:
            n = d[char]
            if n <= n_prev :
                ans += n
            else:
                ans += n - 2 * n_prev
            n_prev = n
        return ans
        
    
    
    