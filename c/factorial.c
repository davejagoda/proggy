#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int factorial(int n)
{
  assert (n >= 0);
  printf("in factorial with n = %d and pointer = %zd\n", n, &n);
  if (n <= 1)
    {
      return (1);
    }
  return (n * factorial(n-1));
}

int main(int argc, char *argv[])
{
  if (argc != 2)
    {
      printf("Usage: %s #\nwhere # is whole number\n", argv[0]);
      return (1);
    }
  printf("%d! = %ld\n", atoi(argv[1]), factorial(atoi(argv[1])));
  return (0);
}
