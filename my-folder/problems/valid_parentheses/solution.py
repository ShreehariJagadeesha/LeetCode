class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
    
        opening=set("([{")
        matching=set([ ("(",")"),("{","}"),("[","]") ])
        st=[]
    
        for i in s:
        
            if i in opening:
                st.append(i)
            
            else:
            
                if len(st)==0:
                    return False
            
                if (st.pop(),i) not in matching:
                    return False
            
        return len(st)==0