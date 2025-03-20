#include <stdbool.h>

bool isPowerOfThree(int n)
{
  if (0 >= n)
    return false;

  while (n % 3 == 0)
  {
    n /= 3;
  }

  return n == 1;
}
