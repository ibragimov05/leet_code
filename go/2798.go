package main

func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
	numberOfEmployee := 0

	for _, hour := range hours {
		if hour >= target {
			numberOfEmployee++
		}
	}

	return numberOfEmployee
}
