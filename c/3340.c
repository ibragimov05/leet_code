#include <stdbool.h>
#include <string.h>

bool isBalanced(char *num)
{
  int odd_sum = 0;
  int even_sum = 0;

  for (int i = 0; i < strlen(num); i++)
  {
    int number = num[i] - '0';
    if (i % 2 == 0)
    {
      even_sum += number;
    }
    else
    {
      odd_sum += number;
    }
  }

  return odd_sum == even_sum;
}
