class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels='aeiou'
        number='0123456789'
        vowel_count=0
        consonants=0

        for i in range(len(s)):
            if s[i] in vowels:
                vowel_count+=1
            elif s[i] in number:
                continue
            elif s[i]==' ':
                continue
            else:
                consonants+=1        
        if(consonants==0):
            return 0
        return(vowel_count//consonants)

        