#include <stdio.h>

int main()
{
  int i = 0;
loop:
  printf("%d\n", i);
  ++i;
  if (i < 10)
    goto loop;
}
