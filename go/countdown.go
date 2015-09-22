package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {
    if 2 != len(os.Args) {
        fmt.Println("need exactly one argument (a non-negative integer)")
	os.Exit(1)
    }
    i, err := strconv.Atoi(os.Args[1])
    if err != nil {
        fmt.Println("conversion to int failed")
	os.Exit(1)
    }
    for i >= 0 {
        fmt.Println(i)
	i--
    }
}
