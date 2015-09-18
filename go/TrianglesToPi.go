package main

import "fmt"
import "math"

// dj@`perl -e 'sub n{ $_ = shift; /^(.)(.*)(.)$/; print $1.length($2).$3,"\n";} n("andreessenhorowitz");'`.com
// idea partially taken from Archimedes

// Imagine a unit circle inscribed with a hexagon
// This hexagon can be split into 6 equilateral triangles
// Each triangle has sides of length 1
// The perimeter of the hex is 6 * 1 = 6
// The circumference of the circle is 2 * π =~ 6.28

// Now imagine the same unit circle inscribed with a 12-gon
// such that the edges and vertices overlap with the hexagon
// the 12-gon can be split into 12 isosceles triangles
// the equal sides have length 1 (unit circle)
// call the length of the other side 's'

// now consider the 2 new triangles which overlap the old triangle
// b will be 1/2 of the old triangles side length
// a is the length from the non-overlapping vertex to the outer edge
// of the old triangle (a picture would be great here).  Then:
// a^2 + b^2 = s^2
// (1-a)^2 + b^2 = 1^2

// need more math here, but upshot is:
// S(n) = sqrt ( 2 - 2 * sqrt (1 - S(n-1)^2 ) )

func main() {
    const DEGREES_IN_CIRCLE = 360
    const SIDES_PER_ITERATION = 6
    const R = 1 // unit circle
    fmt.Println("Triangles to π")
    numSides := SIDES_PER_ITERATION
    theta := float64(DEGREES_IN_CIRCLE) / float64(numSides)
    side := float64(R)
    for i := 0; i <= 20; i++ {
        fmt.Printf("i:%2d number of sides:%32d theta:%33.30f length of side:%33.30f pi:%63.60f\n",
	    i,numSides,theta,side,side*float64(numSides/2));
	numSides = numSides * 2
	theta = float64(DEGREES_IN_CIRCLE) / float64(numSides)
	side = math.Sqrt(float64(float64(2) - float64(2) * math.Sqrt(float64(1) - (float64(side * side) / float64(4) ) ) ) )
    }
}
