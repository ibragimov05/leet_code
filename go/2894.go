package main

func differenceOfSums(n int, m int) int {
	var divisible_by_m int
	var not_divisible_by_m int

	for i := 1; i < n+1; i++ {
		if i%m == 0 {
			divisible_by_m += i
		} else {
			not_divisible_by_m += i
		}
	}

	return not_divisible_by_m - divisible_by_m
}
