class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=['A','E','I','O','U','a','e','i','o','u']
        count_vowels=0
        count_consonant=0
        hash_map={}
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        for key,value in hash_map.items():
            if key in vowels:
                count_vowels=max(value,count_vowels)
            else:
                count_consonant=max(value,count_consonant)
        return count_vowels+count_consonant

        