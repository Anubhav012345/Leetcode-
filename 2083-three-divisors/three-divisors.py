class Solution:
    def isThree(self, n: int) -> bool:
        if n < 2:
            return False
        divisors = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors += 1
                if i != n // i:
                    divisors += 1
        return divisors == 3