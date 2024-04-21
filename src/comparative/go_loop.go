package main

import (
    "fmt"
    "time"
)

func main() {
    start := time.Now()
    for i := 0; i <= 10000; i++ {
        // Do nothing, just loop
    }
    duration := time.Since(start)
    fmt.Println("Go Time:", duration)
}
