#include <stdio.h>

int main(int argc, char *argv[])
{
  while (argc--) {
    printf("%d %s\n", argc, argv[argc]);
  }
}
