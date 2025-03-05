int countElements(int *nums, int numsSize)
{
  for (int i = 0; i < numsSize - 1; i++)
  {
    for (int j = 0; j < numsSize - i - 1; j++)
    {
      if (nums[j] > nums[j + 1])
      {
        int temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }

  int min_num_count = 0;
  int max_num_count = 0;

  for (int i = 0; i < numsSize; i++)
  {
    if (nums[i] == nums[0])
    {
      min_num_count++;
    }

    if (nums[i] == nums[numsSize - 1])
    {
      max_num_count++;
    }
  }

  int result = numsSize - max_num_count - min_num_count;
  return result > 0 ? result : 0;
}
