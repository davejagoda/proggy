#include <stdio.h>

int main()
{
  printf("Precision\n");
  double n = 1;
  int i = 1;
  while (n > 0)
    {
      printf("i:%4d n:%333.330f\n", i , n);
      i++;
      n = n / 2;
    }
}
