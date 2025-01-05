class Solution:
	def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
		result = [0] * k
		uam: dict[int, set] = {}

		for user_id, minute in logs:
			if user_id not in uam:
				uam[user_id] = set()
			uam[user_id].add(minute)

		for active_minutes in uam.values():
			count = len(active_minutes)
			if count <= k:
				result[count - 1] += 1

		return result
