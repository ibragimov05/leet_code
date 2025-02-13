class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
		from datetime import datetime
		return [
			"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][
			datetime(day=day, month=month, year=year).weekday()
		]
