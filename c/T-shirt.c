#include <stdio.h>

int main()
{
  char s[] = "andreessenhorowitz";
  char *p = s;
  int n;
  while (*p != '\0') p++;
  n = p - s - 2;
  printf("%c%d%c\n",
	 s[0], n, s[n + 1]);
  return 0;
}
