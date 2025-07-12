from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # If ransomNote is longer, construction is impossible
        if len(ransomNote) > len(magazine):
            return False

        need = Counter(ransomNote)
        have = Counter(magazine)

        for ch, cnt in need.items():
            if cnt > have[ch]:          # not enough of this letter
                return False
        return True
