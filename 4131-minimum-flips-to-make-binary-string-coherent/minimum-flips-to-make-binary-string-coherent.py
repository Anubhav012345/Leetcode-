class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        c = s.count('1')

        ans = c

        ans = min(ans, n - c)

        if c>0:
            ans = min(ans, c - 1)

        if n>2:
            i_f = 1 if s[0] == '1' else 0
            i_l = 1 if s[n-1] == '1' else 0
            cc = c + 2 - 2*(i_f + i_l)
            ans = min(ans, cc)

        return ans