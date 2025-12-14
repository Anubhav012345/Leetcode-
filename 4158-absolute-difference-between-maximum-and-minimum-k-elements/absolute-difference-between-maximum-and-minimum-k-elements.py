class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        smallest_sum=0
        while i<k:
            smallest_sum+=nums[i]
            i+=1
        j=-1
        largest_sum=0
        while(abs(j)<=k):
            largest_sum+=nums[j]
            j-=1
        
        return(abs(largest_sum-smallest_sum))


        