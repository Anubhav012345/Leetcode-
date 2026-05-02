class Solution:
    def decodeCiphertext(self, s: str, rows: int) -> str:
        if rows == 1:
            return s
        columns = len(s)//rows
        return "".join([s[i::columns+1] for i in range(columns)]).rstrip()