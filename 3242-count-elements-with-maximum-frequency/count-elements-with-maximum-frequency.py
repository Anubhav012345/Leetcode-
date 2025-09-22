class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map={}
        count=0
        for i in range(0,len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        maxi=max(hash_map.values())

        for k,v in hash_map.items():
            if(v==maxi):
                count+=v
        return count 

