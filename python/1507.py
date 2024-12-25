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

        # Extract the numeric part of the day
        day_numeric = "".join(i for i in day if i.isdigit())

        # Format the month with leading zero if necessary
        month_numeric = f"{month_dict[month]:02}"

        # Return the formatted date
        return f"{year}-{month_numeric}-{int(day_numeric):02}"


print(Solution().reformatDate("20th Oct 2052"))
