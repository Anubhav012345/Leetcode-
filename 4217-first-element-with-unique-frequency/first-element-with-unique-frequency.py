class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        
        freq_count = {}
        for value in hash_map.values():
            if value in freq_count:
                freq_count[value] += 1
            else:
                freq_count[value] = 1
        
        for num in nums:
            if freq_count[hash_map[num]] == 1:
                return num
        
        return -1

        
        