import java.lang.Math;

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

public class TrianglesToPi {
    public static final double DEGREES_IN_CIRCLE = 360;
    public static final int SIDES_PER_ITERATION = 6;
    public static final int R = 1; // unit circle
    public static void main(String[] args) {
	System.out.println("Triangles to π");
	int numSides = SIDES_PER_ITERATION;
	double theta = DEGREES_IN_CIRCLE/numSides;
	double side = R;
	for (int i = 0; i <= 15; i++) {
	    System.out.printf("i:%2d number of sides:%8d theta:%13.10f length of side:%13.10f half perimeter:%13.10f%n",
			      i,numSides,theta,side,side*numSides/2);
	    numSides = numSides * 2;
	    theta = DEGREES_IN_CIRCLE/numSides;
	    side = Math.sqrt(2 - 2 * Math.sqrt(1 - (side * side / 4) ) );
	}
    }
}
