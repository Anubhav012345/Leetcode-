class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        c = 0
        v = 0
        for ch in s:
            if 'a' <= ch and ch <= 'z':
                if ch in vowels:
                    v += 1
                else:
                    c += 1
        return 0 if 0 == c else floor(v / c)


        