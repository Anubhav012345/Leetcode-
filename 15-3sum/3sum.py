# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans=[]
#         nums.sort()
#         n=len(nums)
#         for i in range(n):
#             if i!=0 and nums[i]==nums[i-1]:
#                 continue
#             # moving two pointers
#             j=i+1
#             k=n-1
#             while j<k:
#                 total_sum=nums[i]+nums[j]+nums[k]
#                 if total_sum<0:
#                     j+=1
#                 elif(total_sum>0):
#                     k-=1
#                 else:
#                     ans.append([nums[i],nums[j],nums[k]])
#                     j+=1
#                     k-=1
#                 while j<k and nums[j]==nums[j-1]:
#                     j+=1
#                 # if j<k and k==n:
#                 #     break
#                 #     while j<k and nums[k]==nums[k+1]:    
#                 #         k-=1
#         return ans
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res


        