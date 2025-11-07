class Solution:
    def scoreBalance(self, s: str) -> bool:
        s = s.lower().strip()
        n = len(s)

        for k in range(1, n):  # try every possible split position
            string1 = s[:k]
            string2 = s[k:]

            sum1 = 0
            for i in range(len(string1)):
                ascii_val = ord(string1[i])
                score1 = ascii_val - 97 + 1
                sum1 += score1

            sum2 = 0
            for j in range(len(string2)):
                ascii_value1 = ord(string2[j])
                score2 = ascii_value1 - 97 + 1
                sum2 += score2

            if sum1 == sum2:
                return True

        return False
