class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_number=""

        while n>0:
            binary_number=str(n%2)+binary_number
            n//=2
        
        count=binary_number.count('1')
        return count
        