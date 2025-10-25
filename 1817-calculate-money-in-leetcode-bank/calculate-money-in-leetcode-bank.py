class Solution:
    def solve(self,i,total,n,count):
        if(count==n):
            return total
        total+=i
        if(count+1)%7==0:
            next_week=i-(count%7)+1
        else:
            next_week=i+1
        return self.solve(next_week,total,n,count+1)
    def totalMoney(self, n: int) -> int:
        return self.solve(1,0,n,0)
        