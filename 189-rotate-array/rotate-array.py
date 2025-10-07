class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        count=0
        while count!=k:
            e=nums.pop()
            count+=1
            nums.insert(0,e)
        return count
        