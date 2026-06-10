class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        if num1 < 10  :   
            num1 =  3 * '0' + str (num1)   
        elif num1 < 100  :   
            num1 = 2 * '0' + str (num1)   
        elif num1  <= 999 :   
            num1  =  1 * '0' + str (num1)   
        else :   
            num1 =  str (num1)   

        if num2 < 10  :   
            num2 =  3 * '0' + str (num2)   
        elif num2 < 100  :   
            num2 = 2 * '0' + str (num2)   
        elif num2 <= 999 :   
            num2  =  1 * '0' + str (num2)   
        else :   
            num2 =  str (num2)

        if num3 < 10  :   
            num3 =  3 * '0' + str (num3)   
        elif num3 < 100  :   
            num3 = 2 * '0' + str (num3)   
        elif num3  <= 999 :   
            num3  =  1 * '0' + str (num3)   
        else :   
            num3 =  str (num3) 
        string = ''
        for i in range (4)  :  
            result  =  min (num1[i] , num2[i] , num3[i])    
            string  +=  str(result)  
        return  int (string)