
int differenceOfSums(int n, int m)
{
  int divisible_number = 0;
  int not_divisible_number = 0;

  for (int i = 1; i < n + 1; i++)
  {
    if (i % m == 0)
    {
      divisible_number += i;
    }
    else
    {
      not_divisible_number += i;
    }
  }

  return not_divisible_number - divisible_number;
}
