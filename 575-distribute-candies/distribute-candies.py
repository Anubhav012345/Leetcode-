class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        unique=len(set(candyType))
        eat=n//2

        if eat==unique:
            return eat
        elif unique>eat:
            return eat
        else:
            return unique