class Solution:
    def maximumSum(self, nums):
        nums.sort(reverse=True)

        rem = {0: [], 1: [], 2: []}

        for x in nums:
            r = x % 3
            if len(rem[r]) < 3:
                rem[r].append(x)

        ans = 0

        for r in range(3):
            if len(rem[r]) >= 3:
                ans = max(ans, rem[r][0] + rem[r][1] + rem[r][2])

        if rem[0] and rem[1] and rem[2]:
            ans = max(ans, rem[0][0] + rem[1][0] + rem[2][0])

        return ans
