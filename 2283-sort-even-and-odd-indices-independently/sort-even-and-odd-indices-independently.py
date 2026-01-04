class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ans=[]
        i=j=0
        while i<len(even) or j<len(odd):
            if i<len(even):
                ans.append(even[i])
                i+=1
            if j<len(odd):
                ans.append(odd[j])
                j+=1
        return ans
