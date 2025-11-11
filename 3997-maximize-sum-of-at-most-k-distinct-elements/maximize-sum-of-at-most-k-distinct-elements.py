class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        set1=set(nums)
        my_list=list(set1)
        my_list.sort(reverse=True)
        if(len(my_list)<=k):
            return (my_list)
        return(my_list[:k])
        