class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        n=len(nums)
        for k,v in hash_map.items():
            if v>=n/2:
                return k
                
            
        