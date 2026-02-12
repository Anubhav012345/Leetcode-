class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count=0
        zero=0
        for i in range(len(s)):
            if(s[i]=='0'):
                zero+=1
            else:
                if zero>0:
                    count= max(count+1,zero)
                
        return count

        