#include <stdio.h>

int main()
{
  char i = 0;

 loop:
  printf("%d\t", i);
  if (i < 0) { goto end; }
  i++;
  goto loop;

 end:
  printf("\n");
  return 0;
}
