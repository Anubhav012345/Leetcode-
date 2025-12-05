class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        number=0
        for i in range(len(nums)-1):
            number+=nums[i]
            sum_j=sum(nums[i+1:])
            diff=abs(number-sum_j)
            if(diff%2==0):
                count+=1
        return count

        