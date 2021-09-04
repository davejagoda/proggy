#include <locale.h>
#include <stdio.h>
#include <time.h>

/*
try these:
LANG=ja_JP.UTF-8 ./dates_and_locales
LC_ALL=zh_CN.UTF-8 ./dates_and_locales
LC_ALL=zh_TW.UTF-8 ./dates_and_locales
LC_TIME=en_DK.UTF-8 ./dates_and_locales
*/

int main()
{
  time_t t = time(NULL);
  struct tm *tmp;
  tmp = localtime(&t);
  char outstr[512];
  char *current_locale;

  current_locale = setlocale (LC_ALL, "");
  printf("current locale is: %s\n", current_locale);
  strftime(outstr, sizeof(outstr), "%x %X", tmp);
  printf("%s\n", outstr);
}
