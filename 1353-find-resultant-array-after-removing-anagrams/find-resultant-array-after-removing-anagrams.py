class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        prev_sorted = ""  
        for w in words:
            curr_sorted = "".join(sorted(w))
            if curr_sorted != prev_sorted:
                ans.append(w)
                prev_sorted = curr_sorted
        return ans

        