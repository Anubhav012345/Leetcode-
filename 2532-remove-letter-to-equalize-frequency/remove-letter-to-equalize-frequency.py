class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            freq[ch] -= 1

            s = set()

            for val in freq.values():
                if val > 0:
                    s.add(val)

            if len(s) == 1:
                return True

            freq[ch] += 1

        return False