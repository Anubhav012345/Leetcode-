class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash_map={}
        count=0
        for i in range(len(word)):
            hash_map[word[i]]=hash_map.get(word[i],0)+1

        for i in range(len(word)):
            if(word[i]==word[i].upper()):
                if(word[i].lower() in hash_map):
                    count+=1
                    hash_map.pop(word[i].lower())
                    hash_map.pop(word[i].upper())
        return count

        