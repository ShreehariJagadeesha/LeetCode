class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        output=[]
        
        def dfs(l,excluded):
            r=len(l)
            if r<n:
                for c in range(n):
                    if (r,c) in excluded: 
                        continue
                    ex=set()
                    temp="."*c+"Q"+"."*(n-c-1)
                    for r1 in range(r,n):
                        ex.add((r1,c))
                    r2=r3=r
                    c2=c3=c
                    while c2<n:
                        r2=r2+1
                        c2=c2+1
                        ex.add((r2,c2))
                    while c3>0:
                        r3=r3+1
                        c3=c3-1
                        ex.add((r3,c3))
                    dfs(l+[temp],excluded | ex)
            else:
                output.append(l)
        
        dfs([],set())
        
        return output