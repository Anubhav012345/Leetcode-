class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map={}
        for i in range(len(s1)):
            hash_map[s1[i]]=hash_map.get(s1[i],0)+1

        left=0
        window={}

        for r in range(len(s2)):
            window[s2[r]]=window.get(s2[r],0)+1

            if(r - left + 1 > len(s1)):
                window[s2[left]]-=1
                if(window[s2[left]]==0):
                    del window[s2[left]]
                left+=1

            if window==hash_map:
                return True

        return False             


        