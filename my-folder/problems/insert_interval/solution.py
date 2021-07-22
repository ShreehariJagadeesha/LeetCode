class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return [newInterval]
        i=0
        N=len(intervals)
        newstart,newend=newInterval
        output=[]
        
        while i<N and intervals[i][0]<=newstart:
            output.append(intervals[i])
            i=i+1
            
        if not output:
            output.append([newstart,newend])
        elif output[-1][1]<newstart:
            output.append([newstart,newend])
        else:
            output[-1][1]=max(newend,output[-1][1])
        
        while i<N:
            newstart,newend=intervals[i]
            if output[-1][1]<newstart:
                output.append([newstart,newend])
            else:
                output[-1][1]=max(newend,output[-1][1])
            i=i+1
        return output