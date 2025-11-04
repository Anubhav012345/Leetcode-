class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        result=0
        for key,value in hash_map.items():
            if value==k or value%k==0:
                result+=key*value
        return result

        