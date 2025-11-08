class Solution:
    def prime(self,check_number):
        if check_number<=1:
            return False
        i=2
        while i<=check_number//2:
            if check_number%i==0:
                return False
            i+=1
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

        for k,v in hash_map.items():
            if self.prime(v):
                return True
        return False
        