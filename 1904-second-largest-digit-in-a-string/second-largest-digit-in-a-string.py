import re
class Solution:
    def secondHighest(self, s: str) -> int:
        num="1234567890"
        lst=[]
        for i in range(len(s)):
            if s[i] in num:
                lst.append(int(s[i]))
        largest=float("-inf")
        s_largest=float("-inf")
        for num in lst:
            if num>largest:
                s_largest=largest
                largest=num
            elif(num>s_largest and num!=largest):
                s_largest=num
        if s_largest==float("-inf"):
            return -1
        else:
            return s_largest

