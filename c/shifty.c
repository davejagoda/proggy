#include <stdio.h>

/* does C have repeat until?
   no it has do while */

int main()
{
  int i = 0;
  int j = 0;
  int acc = 0;
  printf("exp     current  accumulator\n");
  do
    {
      printf("%2d %12d %12d\n", i, j, acc);
      j = 1 << i;
      acc += j;
      ++i;
    }
  while (j >= 0);
  printf("%2d %12d %12d\n", i, j, acc);
}
