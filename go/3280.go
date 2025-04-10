package main

import (
	"fmt"
	"time"
)

func convertDateToBinary(date string) string {
	parsedDate, _ := time.Parse("2006-01-02", date)

	yearBinary := fmt.Sprintf("%b", parsedDate.Year())
	monthBinary := fmt.Sprintf("%b", parsedDate.Month())
	dayBinary := fmt.Sprintf("%b", parsedDate.Day())

	return fmt.Sprintf("%s-%s-%s", yearBinary, monthBinary, dayBinary)
}
