class Solution:
	def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
		n = len(score)

		for i in range(n):
			swapped = False
			for j in range(n - i - 1):
				if score[j][k] > score[j + 1][k]:
					score[j][k], score[j + 1][k] = score[j + 1][k], score[j][k]
					swapped = True
			if not swapped:
				break

		return score


# def bubble_sort(arr):
# 	n = len(arr)
# 	for i in range(n):
# 		swapped = False
# 		for j in range(n - i - 1):
# 			if arr[j] > arr[j + 1]:
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 				swapped = True
# 		if not swapped:
# 			break  # Stop if already sorted
# 	return arr


print(Solution().sortTheStudents([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]],
                                 2))  # [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
print(Solution().sortTheStudents([[3, 4], [5, 6]], 0))  # [[5,6],[3,4]]
