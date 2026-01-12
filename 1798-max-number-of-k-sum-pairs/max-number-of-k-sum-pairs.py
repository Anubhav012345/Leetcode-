class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map = {}
        count = 0
        for num in nums:
            remaining = k - num
            if hash_map.get(remaining, 0) > 0:
                count += 1
                hash_map[remaining] -= 1
            else:
                hash_map[num] = hash_map.get(num, 0) + 1
        return count
