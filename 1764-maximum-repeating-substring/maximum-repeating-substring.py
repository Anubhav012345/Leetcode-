class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp=word
        count=0 
        while temp in sequence:
            count+=1
            temp+=word
        return count    