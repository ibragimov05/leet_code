#include <string.h>

int romanToInt(char *s)
{
  char roman[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
  int val[7] = {1, 5, 10, 50, 100, 500, 1000};

  int result_sum = 0;
  int previous_val = 0;

  for (int i = strlen(s) - 1; i >= 0; i--)
  {
    int current_value = 0;

    for (int j = 0; j < 7; j++)
    {
      if (roman[j] == s[i])
      {
        current_value = val[j];
        break;
      }
    }

    if (previous_val > current_value)
    {
      result_sum -= current_value;
    }
    else
    {
      result_sum += current_value;
    }
    previous_val = current_value;
  }

  return result_sum;
}
