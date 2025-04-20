package main

func getFinalState(nums []int, k int, multiplier int) []int {
	for range k {
		index := FindFirstMinimumNumber(&nums)
		nums[index] *= multiplier
	}

	return nums
}

func FindFirstMinimumNumber(arr *[]int) int {
	minIndex := 0

	for i := range *arr {
		if (*arr)[minIndex] > (*arr)[i] {
			minIndex = i
		}
	}

	return minIndex
}
