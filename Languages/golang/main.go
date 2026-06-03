package main

import (
	"fmt"
)

func main() {
	//how to print in go:
	fmt.Println("Hello, World!")

	//how to declare variables in go:
	//int, string, float, boolean,int64, float32, float64,int8,uint8,uint16,uint32,uint64,byte,rune,complex64,complex128
	var a int = 10
	b := 20
	c := "Go Programming"
	d := 3.14//float64
	e := true //boolean
	fmt.Println("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

	//type conversion in go:
	in := 42
	fl := float64(in)
	
	//sprintf usage in go:
	s := fmt.Sprintf("I am %v years old", 10)// I am 10 years old
	s := fmt.Sprintf("I am %v years old", "way too many")// I am way too many years old
	
	//if-else statement in go:
	if a > b {
		fmt.Println("a is greater than b")
	}else if a == b {
		fmt.Println("a is equal to b")
	}else {
		fmt.Println("a is not greater than b")
	}

	//inputs in go:
	var name string
	fmt.Print("Enter your name: ")
	fmt.Scanln(&name)
	fmt.Println("Hello,", name)

	//switch-case in go:
	var day	int
	fmt.Print("Enter day number (1-7): ")
	fmt.scanln(&day)
	switch day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6:
		fmt.Println("Saturday")
	case 7:
		fmt.Println("Sunday")
	default:
		fmt.Println("Another day")
	}

	//functions in go:
	func add(x int, y int) int {
		return x + y
	}
	fmt.Println("Sum:", add(5, 10))
	
	//named return values in go:
	func swap(a, b string) (x, y string) {
		x = b
		y = a
		return
	}
	s1, s2 := swap("hello", "world")
	fmt.Println("s1:", s1, "s2:", s2)

	//naked return values in go:
	func calc(a, b int) (mul,div int,err error) {
		if b == 0 {
			return 0, 0, fmt.Errorf("division by zero")
		}
		mul = a * b
		div = a / b
		return mul, div, nil
	}
	m, d, err := calc(10, 2)
	
	//
}
