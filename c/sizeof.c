#include <stdio.h>

int main()
{
  printf("sizeof(%s): %lu\n", "char", sizeof(char));
  printf("sizeof(%s): %lu\n", "short", sizeof(short));
  printf("sizeof(%s): %lu\n", "int", sizeof(int));
  printf("sizeof(%s): %lu\n", "long", sizeof(long));
}
