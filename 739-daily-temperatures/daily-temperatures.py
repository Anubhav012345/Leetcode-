class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n=len(temperatures)
        # ans=[0]*n
        # stack=[]
        # for i in range(n):
        #     while(len(stack)!=0)and temperatures[i]>temperatures[stack[-1]]:
        #         stack.pop()
        #     if(len(stack)!=0):
        #         ans[i]=stack[-1]-i
        #     stack.append(i)
        # return ans
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            # Compare with the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans