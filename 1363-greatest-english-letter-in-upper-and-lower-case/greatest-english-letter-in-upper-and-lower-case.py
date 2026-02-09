class Solution:
    def greatestLetter(self, s: str) -> str:
        hash_map={}
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1

        lst=[]
        for i in range(len(s)):
            if(s[i].isupper()):
                if(s[i].lower() in hash_map):
                    lst.append(s[i])
        if(len(lst)==0):
            return ''
        lst.sort()
        return(lst[-1])

        