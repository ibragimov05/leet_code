package main

func scoreOfString(s string) int {
	score := 0

	for i := range len(s) - 1 {
		box := int(s[i]) - int(s[i+1])

		if box < 0 {
			box = -box
		}

		score += box
	}

	return score
}
