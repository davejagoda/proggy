#include <stdio.h>
#include <math.h>

int main()
{
  const double DEGREES_IN_CIRCLE = 360;
  const int SIDES_PER_ITERATION = 6;
  const int R = 1; // unit circle
  printf("Triangles to π\n");
  int numSides = SIDES_PER_ITERATION;
  double theta = DEGREES_IN_CIRCLE/numSides;
  double side = R;
  for (int i = 0; i <= 20; i++) {
    printf("i:%2d number of sides:%8d theta:%13.10f length of side:%13.10f half perimeter:%13.10f\n",
		      i,numSides,theta,side,side*numSides/2);
    numSides = numSides * 2;
    theta = DEGREES_IN_CIRCLE/numSides;
    side = sqrt(2 - 2 * sqrt(1 - (side * side / 4) ) );
  }
}
