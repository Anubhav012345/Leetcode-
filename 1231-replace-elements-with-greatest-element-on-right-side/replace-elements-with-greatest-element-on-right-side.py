class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * n
        n -= 2
        m = arr[n+1]
        for i in range(n, -1, -1):
            result[i] = m
            if arr[i] > m:
                m = arr[i]

        return result