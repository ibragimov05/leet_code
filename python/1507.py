class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12,
        }

        day, month, year = date.split()
        day_numeric = "".join(i for i in day if i.isdigit())
        month_numeric = f"{month_dict[month]:02}"

        return f"{year}-{month_numeric}-{int(day_numeric):02}"
