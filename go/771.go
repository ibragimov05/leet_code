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
