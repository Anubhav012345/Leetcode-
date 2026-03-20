class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0

        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

        count=0
        if k==0:
            for num in hash_map:
                if hash_map[num]>1:
                    count+=1
                
        else:
            for num in hash_map:
                if num+k in hash_map:
                    count+=1

        return count
