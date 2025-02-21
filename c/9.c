int isPalindrome(int x)
{
  if (x < 0)
  {
    return 0;
  }

  if (x < 10)
  {
    return 1;
  }

  long reversed = 0;
  int original = x;

  while (x > 0)
  {
    reversed = reversed * 10 + x % 10;
    x /= 10;
  }

  return reversed == original;
}
