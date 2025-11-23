class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map={}

        for i in range(len(numbers)):
            remaining=target-numbers[i]
            if remaining in hash_map:
                return([hash_map[remaining]+1,i+1])
            hash_map[numbers[i]]=i
        

            
        