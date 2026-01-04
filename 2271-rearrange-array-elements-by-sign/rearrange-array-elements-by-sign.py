class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        i=j=0
        ans=[]
        while i<len(pos) and j<len(neg):
            ans.append(pos[i])
            ans.append(neg[j])
            i += 1
            j += 1
        return ans
