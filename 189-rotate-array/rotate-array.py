class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    #     n=len(nums)
    #     k=k%n

    #     self.reverse(nums,0,n-1)

    #     self.reverse(nums,0,k-1)

    #     self.reverse(nums,k,n-1)
       
       
    # def reverse(self,arr,left,right):
    #     while left<right:
    #         arr[left],arr[right] = arr[right] , arr[left]
    #         left+=1
    #         right-=1

    # Approach 2nd
        # n=len(nums)
        # rotations=k%n
        # j=n-rotations
        # nums[:]=nums[j:n]+nums[0:j]
        # return nums
    
    
    # Approach 3rd
        n=len(nums)
        rotations=k%n
        for _ in range(0,rotations):
            e=nums.pop()
            nums.insert(0,e)
        return nums


        