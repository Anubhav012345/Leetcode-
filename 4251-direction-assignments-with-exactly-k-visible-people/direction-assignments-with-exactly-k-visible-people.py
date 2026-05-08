class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod_val = 1000000000 + 7
        return (math.comb(n-1, k)*2)%mod_val
                