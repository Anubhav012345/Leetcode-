class Solution:
    def longestBalanced(self, s: str) -> int:
        length=0

        for i in range(len(s)):
            hash_map={}

            for j in range(i,len(s)):
                hash_map[s[j]]=hash_map.get(s[j],0)+1

                flag=True
                freq=-1

                for value in hash_map.values():
                    if(freq==-1):
                        freq=value
                    elif(value!=freq):
                        flag=False
                        break
                
                if(flag):
                    length=max(length,j-i+1)

        return length
        