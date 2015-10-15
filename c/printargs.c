#include <stdio.h>

int main(int argc, char *argv[])
{
  for (int i = 0; i < argc; ++i)
    {
      printf("argument #%d was: %s\n", i, argv[i]);
    }
}
