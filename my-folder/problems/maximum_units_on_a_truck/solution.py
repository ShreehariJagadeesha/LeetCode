class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda x: -x[1])
        capacity=0
        for box,unit in boxTypes:
            if truckSize>=box:
                truckSize-=box
                capacity+=box*unit
            else:
                capacity+=truckSize*unit
                break
        return capacity
                
        
        