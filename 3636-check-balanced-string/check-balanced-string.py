class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum=0
        odd_sum=0
        num=[int(d) for d in str(num)]
        for i in range(len(num)):
            if i%2==0:
                even_sum+=num[i]
            else:
                odd_sum+=num[i]
        if(even_sum==odd_sum):
            return True
        return False