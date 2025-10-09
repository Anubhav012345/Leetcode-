class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                if 'A' <= ch <= 'Z':
                    ch = chr(ord(ch) + 32)
                result += ch
        left = 0
        right = len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True
