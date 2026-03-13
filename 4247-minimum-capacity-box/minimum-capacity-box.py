class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        maxi=float("inf")
        index=-1

        for i in range(len(capacity)):
            if(capacity[i]>=itemSize):
                if(maxi>capacity[i]):
                    maxi=capacity[i]
                    index=i

        return index

        