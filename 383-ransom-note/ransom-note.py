class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map={}
        for i in range(len(magazine)):
            hash_map[magazine[i]]=hash_map.get(magazine[i],0)+1

        for ch in ransomNote:
            if hash_map.get(ch,0)==0:
                return False
            hash_map[ch]-=1
        
        return True


        