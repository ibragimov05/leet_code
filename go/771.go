package main

import "strings"

func numJewelsInStones(jewels string, stones string) int {
	jewelsCount := 0

	for _, stone := range stones {
		if strings.ContainsRune(jewels, stone) {
			jewelsCount++
		}
	}

	return jewelsCount
}

// jewels_count = 0
//         for stone in stones:
//             if stone in jewels:
//                 jewels_count += 1
//         return jewels_count
