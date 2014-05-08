#include <stdio.h>

int main()
{
  char s[] =  "andreessenhorowitz";
  char *p = s;
  while (*p != '\0') p++;
  printf("%c%ld%c\n", s[0], p - s - 2, s[p - s - 1]);
  return 0;
}
