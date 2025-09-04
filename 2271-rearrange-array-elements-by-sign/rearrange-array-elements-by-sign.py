class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst=[]
        lst1=[]
        for i in range(len(nums)):
            if(nums[i]>0):
                lst.append(nums[i])
            else:
                lst1.append(nums[i])
        # merged=[]
        # for i,j in zip(lst,lst1):
        #     merged.append(lst)
        #     merged.append(lst1)
        merged = [x for pair in zip(lst, lst1) for x in pair]
        return merged



        