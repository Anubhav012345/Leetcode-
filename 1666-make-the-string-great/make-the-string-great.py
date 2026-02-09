class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if(len(stack)==0 or 
            (stack[-1]!= s[i].lower() and stack[-1]!=s[i].upper()) or 
            (stack[-1]==s[i])):
                stack.append(s[i])
            else:
                stack.pop()
        
        lst=[]
        while stack:
            e=stack.pop()
            lst.append(e)

        lst.reverse()

        return "".join(lst)
        
        
