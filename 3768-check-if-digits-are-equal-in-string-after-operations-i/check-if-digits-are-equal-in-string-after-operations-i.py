class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if(len(s)==2):
            return s[0]==s[1]
        num=[int(ch) for ch in s]
        while(len(num)>2):
            new_nums=[]
            for i in range(len(num)-1):
                j=i+1
                new_nums.append((num[i]+num[j])%10)
            num=new_nums
        return num[0]==num[1]
