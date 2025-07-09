class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        length=len(digits)+1
        my_list=[0]*length
        my_list[0]=1
        return my_list




        