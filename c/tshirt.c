#include <stdio.h>

char s[] =
  "andreessenhorowitz";

int main()
{
  printf("%c%d%c\n",
	 s[0],
	 1<<4,
	 s[sizeof(s)-2]);
}
