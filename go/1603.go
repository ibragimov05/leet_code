package main

type ParkingSystem struct {
	capacity []int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{capacity: []int{big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if this.capacity[carType-1] > 0 {
		this.capacity[carType-1]--

		return true
	} else {
		return false
	}
}
