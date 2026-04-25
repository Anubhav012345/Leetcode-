class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        if str(x) in s and str(x) != s[0]:
            return True
        return False