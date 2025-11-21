class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        factor = 1
        parts = []
        while n > 0:
            rem = n % 10
            if rem != 0:
                parts.append(rem * factor)
            n //= 10
            factor *= 10
        return parts[::-1]
