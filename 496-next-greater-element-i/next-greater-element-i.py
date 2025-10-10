class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, next_greater = [], {}
        for n in nums2:
            while stack and n > stack[-1]:
                next_greater[stack.pop()] = n
            stack.append(n)
        return [next_greater.get(x, -1) for x in nums1]
