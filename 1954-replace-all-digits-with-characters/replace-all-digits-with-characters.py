class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        last_char_ascii = 0
        
        for char in s:
            if char.isalpha():
                result += char
                last_char_ascii = ord(char)
            else:
                shift_amount = int(char)
                result += chr(last_char_ascii + shift_amount)
                
        return result