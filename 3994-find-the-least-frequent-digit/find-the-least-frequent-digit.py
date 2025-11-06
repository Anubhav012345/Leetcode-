class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        lst=[]
        while n!=0:
            temp=n%10
            lst.append(temp)
            n=n//10
        lst.sort()
        hash_map={}
        for i in range(len(lst)):
            hash_map[lst[i]]=hash_map.get(lst[i],0)+1
        min_freq=float("inf")
        for k,v in hash_map.items():            
            min_freq=min(min_freq,v)
        
        for k,v in hash_map.items():
            if v==min_freq:
                return k

        
        