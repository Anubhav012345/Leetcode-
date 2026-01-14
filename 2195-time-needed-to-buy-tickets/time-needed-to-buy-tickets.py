from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append((tickets[i],i))
        count=0
        while q:
            temp,idx=q.popleft()
            temp-=1
            count+=1

            if idx==k and temp==0:
                break
            
            if temp>0:
                q.append((temp,idx))
        return count


        
        