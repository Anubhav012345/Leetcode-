class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        hash_map={}
        for i in range(len(bulbs)):
            hash_map[bulbs[i]]=hash_map.get(bulbs[i],0)+1
        
        lst=[]
        for key,value in hash_map.items():
            if(value%2!=0):
                lst.append(key)
            
        lst.sort()
        return lst

        