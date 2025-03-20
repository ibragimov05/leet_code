#include <stdbool.h>

bool isPowerOfFour(int n)
{
  if (0 >= n)
    return false;

  while (n % 4 == 0)
  {
    n /= 4;
  }

  return n == 1;
}
