class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        res = []
        for i,j in c.items():
            res.append((j , i))
			# [(2,'a) , (1,'e) , (1,'t)]
        res.sort(key = lambda x: x[0] , reverse =True)
		#Sorting on the basis of first index(0 - Index) 
        ans = ''
        for i,j in res:
            ans+= j*i
        return (ans)