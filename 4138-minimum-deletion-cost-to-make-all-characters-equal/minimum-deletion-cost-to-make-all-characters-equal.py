class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        sm = sum(cost)
        d = defaultdict(lambda: sm)

        for ch, chCost in zip(s, cost):
            d[ch]-= chCost

        return min(d.values())    