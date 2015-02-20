package main

import (
    "fmt"
    "math/rand"
)

func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
    fmt.Println("Your favorite number is", rand.Intn(10))
}
