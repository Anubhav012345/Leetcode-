class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        week_start=1
        day=0
        for _ in range(n):
            total+=week_start+day
            day+=1
            if(day==7):
                week_start+=1
                day=0
        return total
        