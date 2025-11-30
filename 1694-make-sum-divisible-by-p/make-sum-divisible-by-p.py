class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        answer = len(nums)

        for i in range(len(nums)):
            num = nums[i]
            prefix = (prefix + num) % p
            needed = (prefix - target) % p

            if needed in seen:
                answer = min(answer, i - seen[needed])

            seen[prefix] = i

        # return must be AFTER the loop
        return answer if answer < len(nums) else -1
