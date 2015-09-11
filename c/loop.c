/* gcc -o loop loop.c */

#include <stdio.h>

#define DEBUG 1

int main() {
  int i = 1;
  int max = 1;
  int min = 1;
  while (i) {
#ifdef DEBUG
    if (i % (512 * 1024 * 1024) == 0) printf("i: %12d\n", i);
#endif
    ++i;
    if (i < min) min = i;
    if (i > max) max = i;
  }
  printf("infinite loop ended\n");
  printf("max: %d min: %d\n", max, min);
}
