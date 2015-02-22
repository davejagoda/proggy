package main

import "fmt"

func integerDivision(dividend, divisor int) (quotient, remainder int) {
    quotient = dividend / divisor
    remainder = dividend % divisor
    return
}

func main() {
    fmt.Println(integerDivision(255, 2))
}
