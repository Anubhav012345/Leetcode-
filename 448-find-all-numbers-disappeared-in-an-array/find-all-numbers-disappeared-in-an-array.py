class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_map={}        
        for num in nums:
            hash_map[num]=hash_map.get(num, 0) + 1
        
        result = []
        for i in range(1, len(nums) + 1):
            if i not in hash_map:
                result.append(i)
        
        return result