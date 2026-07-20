from typing import List
class Solution:
    def canReach(self, start: List[int], target: List[int]) -> bool:
        start_color = (start[0] + start[1]) % 2
        target_color = (target[0] + target[1]) % 2

        return start_color == target_color