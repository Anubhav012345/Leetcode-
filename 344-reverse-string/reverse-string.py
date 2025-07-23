class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack=[]
        for j in s:
            stack.append(j)
        for i in range(len(s)):
            s[i]=stack.pop()