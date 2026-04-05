class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")
        d = moves.count("_")
        answer = 0
        
        if l>r:
            answer = -(l+d) + r
        else:
            answer = (r+d) -l
        
        return abs(answer)
            


        