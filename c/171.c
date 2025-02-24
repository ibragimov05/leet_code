#include <string.h>

int titleToNumber(char *columnTitle)
{
  int result = 0;
  int char_length = strlen(columnTitle);

  for (int i = 0; i < char_length; i++)
  {
    result = result * 26 + (((int)columnTitle[i]) - ((int)'A') + 1);
  }

  return result;
}
