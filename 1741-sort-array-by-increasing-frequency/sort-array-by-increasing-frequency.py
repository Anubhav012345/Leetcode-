class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

        def get_value(item):
            return(item[1],-item[0])

        items=sorted(hash_map.items(),key=get_value)

        res=[]
        for key,value in items:
            for _ in range(value):
                res.append(key)

        return res
        