class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in range(len(logs)):
            if(logs[i]=='../'):
                if(len(stack)!=0):
                    stack.pop()
            elif(logs[i]=='./'):
                continue
            else:
                stack.append(logs[i])
        
        return len(stack)
        