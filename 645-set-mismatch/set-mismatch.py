class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        
        maximum_num=len(nums)
        total=int((maximum_num)*(maximum_num+1)/2)
        
        sumation=0
        lst=[]
        for key, value in hash_map.items():
            if(value==2):
                lst.append(key)
            sumation+=key
        lst.append(total-sumation)

        return lst
            
        
        