class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1=[]
        temp=""
        for ch in version1:
            if(ch=='.'):
                lst1.append(temp)
                temp=""
            else:
                temp+=ch
        lst1.append(temp)

        lst2=[]
        temp2=""
        for char in version2:
            if(char =='.'):
                lst2.append(temp2)
                temp2=""
            else:
                temp2+=char
        lst2.append(temp2)

        length1=len(lst1)
        length2=len(lst2)
        n=max(length1,length2)

        for i in range(n):
            
            if i<length1:
                v1=int(lst1[i])
            else:
                v1=0
            
            if i<length2:
                v2=int(lst2[i])
            else:
                v2=0
        
            if(v1 < v2):
                return -1
            
            if(v1 > v2):
                return 1
            
        return 0



        

        