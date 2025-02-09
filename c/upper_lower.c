#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
  int arg_index, string_index;
  arg_index = 1;
  while (arg_index < argc) {
    printf("original: %s\n", argv[arg_index]);
    printf("upper: ");
    for (string_index = 0; string_index < strlen(argv[arg_index]);
         ++string_index) {
      printf("%c", (toupper(argv[arg_index][string_index])));
    }
    printf("\n");
    printf("lower: ");
    for (string_index = 0; string_index < strlen(argv[arg_index]);
         ++string_index) {
      printf("%c", (tolower(argv[arg_index][string_index])));
    }
    printf("\n\n");
    ++arg_index;
  }
}
