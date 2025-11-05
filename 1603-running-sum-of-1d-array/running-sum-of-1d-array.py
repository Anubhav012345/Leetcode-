class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            add=sum(nums[:i+1])
            lst.append(add)
        return lst
        