package main

func getConcatenation(nums []int) []int {
	lenNums := len(nums)
	concatenation := make([]int, lenNums*2)

	for i := range concatenation {
		concatenation[i] = nums[i%lenNums]
	}

	return concatenation
}
