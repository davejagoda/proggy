#include <stdio.h>
#include <unistd.h>

int main()
{
  printf("hello from pid %d\n", getpid());
}
