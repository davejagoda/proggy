#include <stdio.h>
#include <time.h>

int print_time(time_t t)
{
  printf("epoch %11ld time is %s", t, asctime(gmtime(&t)));
  return(0);
}

int main()
{
  time_t t = time(NULL);
  print_time(t);
  t = 0;
  print_time(0);
  print_time(t);
  t = 1 << 31;
  print_time(1 << 31);
  print_time(t);
  t = -t;
  print_time(-1 * (1 << 31));
  print_time(t);
}
