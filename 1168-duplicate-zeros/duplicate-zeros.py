class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lst=[]
        for i in range(len(arr)):
            if(len(arr)==len(lst)):
                break
            else:
                if(arr[i]!=0):
                    lst.append(arr[i])
                else:
                    lst.append(arr[i])
                    lst.append(arr[i])
        for i in range(len(arr)):
            arr[i]=lst[i]
        return arr