class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        result=[]
        carry=0
        for i in range(max(len(num1),len(num2))):
            val1=num1[len(num1)-1-i] if i<len(num1) else 0
            val2=num2[len(num2)-1-i] if i<len(num2) else 0
            reminder=(int(val1)+int(val2)+carry)%10
            carry=(int(val1)+int(val2)+carry)//10
            result.append(str(reminder))
        if carry!=0:
            result.append(str(carry))
        
        return ''.join(reversed(result))