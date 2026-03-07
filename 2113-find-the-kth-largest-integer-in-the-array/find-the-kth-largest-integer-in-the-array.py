class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lst=[]
        for i in range(len(nums)):
            lst.append(int(nums[i]))

        lst.sort(reverse=True)
        
        return(str(lst[k-1]))