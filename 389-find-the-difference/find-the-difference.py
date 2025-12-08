class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        asci=0
        for i in range(len(s)):
            ascii_store=ord(s[i])
            asci+=ascii_store
        
        target=0
        for i in range(len(t)):
            ascii_store=ord(t[i])
            target+=ascii_store

        targetchar=target-asci

        return chr(targetchar)
        

        


        