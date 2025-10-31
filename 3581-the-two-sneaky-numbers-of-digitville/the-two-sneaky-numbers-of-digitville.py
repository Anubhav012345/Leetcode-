class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        lst=[]
        for k,v in hash_map.items():
            if(v==2):
                lst.append(k)
        return lst
        