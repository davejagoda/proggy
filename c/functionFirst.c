#include <stdio.h>

/* C requires the function to be defined first */

int fun()
{
  printf("inside function fun\n");
  return(0);
}

int main()
{
  fun();
  printf("hello function first\n");
}
