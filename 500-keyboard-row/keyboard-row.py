class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"

        lst=[]

        for i in range(len(words)):
            first_word=words[i].lower()

            if first_word[0] in first_row:
                row=first_row
            elif first_word[0] in second_row:
                row=second_row
            else:
                row=third_row

            j=0
            for j in range(len(first_word)):
                if first_word[j] not in row:
                    break
                
                if j==len(first_word)-1:
                    lst.append(words[i])

        return lst


        