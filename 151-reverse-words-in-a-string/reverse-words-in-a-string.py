class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        j=len(lst)-1
        i=0
        while i<j:
            lst[i],lst[j]=lst[j],lst[i]
            j-=1
            i+=1
        result=' '.join(lst)
        return result
        
        