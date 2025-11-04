class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])


        lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            lst[1] = 29

        totalcount = sum(lst[:month - 1]) + day
        return totalcount
