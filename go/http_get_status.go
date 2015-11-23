package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    for i := 1; i < len(os.Args); i++ {
        fmt.Println(os.Args[i])
        resp, err := http.Head("http://" + os.Args[i])
        fmt.Println(resp)
        if err != nil {
            fmt.Println(err)
        }
    }
}
