#include <stdio.h>
#include <math.h>

int main()
{
  const long double DEGREES_IN_CIRCLE = 360;
  const int SIDES_PER_ITERATION = 6;
  const int R = 1;		// unit circle
  printf("Triangles to π\n");
  long int numSides = SIDES_PER_ITERATION;
  long double theta = DEGREES_IN_CIRCLE / numSides;
  long double side = R;
  for (int i = 0; i <= 20; i++) {
    printf
	("i:%2d number of sides:%8ld theta:%23.20Lf length of side:%23.20Lf half perimeter:%23.20Lf\n",
	 i, numSides, theta, side, side * (numSides / 2));
    numSides = numSides * 2;
    theta = DEGREES_IN_CIRCLE / numSides;
    side = sqrt(2 - 2 * sqrt(1 - (side * side / 4)));
  }
}
