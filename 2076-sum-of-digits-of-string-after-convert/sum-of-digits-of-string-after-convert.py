class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for ch in s:
            num+=str(ord(ch)-96)
        x=sum(int(d) for d in num)

        for _ in range(k - 1):
            x=sum(int(d) for d in str(x))
        return x
