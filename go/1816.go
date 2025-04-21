package main

import "strings"

func truncateSentence(s string, k int) string {
	words := strings.Fields(s)

	words = words[:k]

	return strings.Join(words, " ")
}
