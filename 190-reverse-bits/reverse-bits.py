class Solution:
    def reverseBits(self, n: int) -> int:
        num_string=''

        for _ in range(32):
            num_string=str(n%2)+num_string
            n//=2
        
        reverse_string=num_string[::-1]
        num=0

        for digit in reverse_string:
            num=(num*2)+int(digit)
        
        return num

        
        