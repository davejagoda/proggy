// inspired by this:
// http://patshaughnessy.net/2015/9/25/what-do-perl-and-go-have-in-common
// area formula from Wikipedia: https://en.wikipedia.org/wiki/Regular_polygon

package main

import (
  "fmt"
  "math"
)

type RegularPolygon struct {
  n uint64  // number of sides
  s float64 // side length
}

func (self RegularPolygon) Perimeter() float64 {
  return float64(self.n) * self.s
}

func (self RegularPolygon) Area() float64 {
  return ( float64(self.n) * self.s * self.s ) / ( math.Tan(math.Pi / float64(self.n) ) * 4 )
}

func main() {
  triangle := RegularPolygon { 3, 1 }
  square   := RegularPolygon { 4, 1 }
  fmt.Println("The perimeter of an equilateral triangle with side length of 1 is :", triangle.Perimeter())
  fmt.Println("The area of an equilateral triangle with side length of 1 is :", triangle.Area())
  fmt.Println("The perimeter of a square with side length of 1 is :", square.Perimeter())
  fmt.Println("The area of a square with side length of 1 is :", square.Area())
}
