class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # i=0
        # j=0
        # fruits.sort()
        # baskets.sort()
        # while i<len(fruits) and j<len(baskets):
        #     if(fruits[i]<baskets[j]):
        #         i+=1
        #     j+=1
        # return len(fruits)-i
        count=0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if(fruits[i]<=baskets[j]):
                    fruits[i]=0
                    baskets[j]=0
                    break
        for i in range(len(fruits)):
            if(fruits[i]!=0):
                count+=1
        return count



        