class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

        sorted_dict = dict(sorted(hash_map.items(), key=lambda x: x[1]))

        for key,value in sorted_dict.items():
            if(key%2==0):
                if(value%2!=0):
                    return key

        return -1

        