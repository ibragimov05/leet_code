class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		from datetime import datetime
		print(datetime(day=day, month=month, year=year))
		return ''


print(Solution().dayOfTheWeek(day=31, month=8, year=2019))
print(Solution().dayOfTheWeek(day=18, month=7, year=1999))
print(Solution().dayOfTheWeek(day=15, month=8, year=1993))

# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
#
#
#
# Example 1:
#
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# Example 2:
#
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# Example 3:
#
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
