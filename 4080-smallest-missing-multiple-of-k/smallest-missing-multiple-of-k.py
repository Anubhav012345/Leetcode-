class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash_map={}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                continue
            else:
                hash_map[nums[i]]=i
        i = 1
        while True:
            if (k * i) not in hash_map:
                return k * i
            i += 1
