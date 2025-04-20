package main

func getFinalState(nums []int, k int, multiplier int) []int {
	for range k {
		minIndex := 0

		for i := range nums {
			if (nums)[minIndex] > (nums)[i] {
				minIndex = i
			}
		}

		nums[minIndex] *= multiplier
	}

	return nums
}
