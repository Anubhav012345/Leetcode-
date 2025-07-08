class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2_set = set(nums2)
        for num in set(nums1):
            if num in nums2_set:
                result.append(num)
        return result
