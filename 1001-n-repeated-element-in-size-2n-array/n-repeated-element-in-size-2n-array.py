class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1

        for key,value in hash_map.items():
            if value>1:
                return key
                break
        

        