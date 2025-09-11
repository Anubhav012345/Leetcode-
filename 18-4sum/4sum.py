class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        my_set=set()
        n=len(nums)
        if n<4:
            return[]
        else:
            for i in range(0,n):
                for j in range(i+1,n):
                    hash_set=set()
                    for k in range(j+1,n):
                        fourth=target-(nums[i]+nums[j]+nums[k])
                        if fourth in hash_set:
                            lst=[nums[i],nums[j],nums[k],fourth]
                            lst.sort()
                            my_set.add(tuple(lst))
                        hash_set.add(nums[k])
        ans=list(my_set)
        return ans
        