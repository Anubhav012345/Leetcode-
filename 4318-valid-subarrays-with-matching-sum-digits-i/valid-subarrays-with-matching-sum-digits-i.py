class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        N = len(nums)
        cnt = 0
        for l in range(N):
            sm = 0
            for r in range(l, N):
                sm += nums[r]
                cnt += str(sm)[0] == str(sm)[-1] == str(x)
        return cnt