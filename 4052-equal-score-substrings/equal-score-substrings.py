class Solution:
    def scoreBalance(self, s: str) -> bool:
        s = s.lower().strip()
        total = sum(ord(ch) - 97 + 1 for ch in s)
        left_sum = 0

        for i in range(len(s)):
            left_sum += ord(s[i]) - 97 + 1
            right_sum = total - left_sum
            if left_sum == right_sum:
                return True
        return False
