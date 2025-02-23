int subarraySum(int *nums, int numsSize)
{
  int sub_sum = 0;

  for (int i = 0; i < numsSize; i++)
  {
    int start = i - nums[i] > 0 ? i - nums[i] : 0;

    for (int j = start; j < i + 1; j++)
    {
      sub_sum += nums[j];
    }
  }

  return sub_sum;
}
