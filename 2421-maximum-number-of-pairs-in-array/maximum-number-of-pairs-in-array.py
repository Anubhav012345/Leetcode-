class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        pair=0
        left=0
        for key, value in hash_map.items():
            if(value%2==0):
                pair+=int(value/2)
            elif(value>2):
                group=value-1
                pair+=int(group/2)
                left+=1
            else:
                left+=1

        lst=[]
        lst.append(pair)
        lst.append(left)
        return lst

        