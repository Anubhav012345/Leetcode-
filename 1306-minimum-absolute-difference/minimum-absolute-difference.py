class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini=float("inf")
        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            mini=min(mini,diff)
        
        ans=[]
        for i in range(len(arr)-1):
            if(abs(arr[i+1]-arr[i])==mini):
                ans.append([arr[i],arr[i+1]])
        return ans
        