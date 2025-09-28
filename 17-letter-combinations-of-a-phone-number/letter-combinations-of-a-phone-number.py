class Solution:
    def solve(self,index,subset,char_map,digits,result):
        if len(digits)<=index:
            result.append("".join(subset))
            return
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,char_map,digits,result)
            subset.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        char_map={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result=[]
        self.solve(0,[],char_map,digits,result)
        return result
        