class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         a=0
#         l=0
        
#         for x in s:
#             if x=='A':
#                 a=a+1
#                 l=0
#             elif x=='L':
#                 l=l+1
#             else:
#                 l=0
#         if a>1 or l>2:
#             return False
#         return True
        return True if (s.count("LLL")<1 and s.count("A")<2) else False