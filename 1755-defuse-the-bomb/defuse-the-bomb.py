class Solution:
    def decrypt(self, code, k):
        n = len(code)
        lst = [0] * n
        if k == 0:
            return lst
        for i in range(n):
            j = i
            add = 0
            if k>0:
                count=0
                while count<k:
                    j=(j+1)%n
                    add+=code[j]
                    count+=1
            else:
                count=0
                while count<-k:
                    j =(j-1+ n)%n
                    add+=code[j]
                    count+=1
            lst[i]=add
        return lst
