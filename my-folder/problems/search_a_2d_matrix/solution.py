class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        Rows=len(matrix)
        Cols=len(matrix[0])
        
        top=0
        bot=Rows-1
        
        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        
        if not(top<=bot):
            return False
        
        row=(top+bot)//2
        
        l=0
        r=Cols
        
        while l<=r:
            mid=(l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True
            
        return False