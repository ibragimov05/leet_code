#include <stdio.h>
#include <stdlib.h>

void _inset_number(int arr[], int *array_size, int pos, int val)
{
  for (int i = *array_size; i > pos; i--)
    arr[i] = arr[i - 1];

  arr[pos] = val;
  (*array_size)++;
}

int *createTargetArray(int *nums, int numsSize, int *index, int indexSize, int *returnSize)
{
  int *target_array = (int *)malloc(numsSize * sizeof(int));
  int current_size = 0;

  if (target_array == NULL)
  {
    *returnSize = 0;
    return NULL;
  }

  for (int i = 0; i < numsSize; i++)
  {
    _inset_number(target_array, &current_size, index[i], nums[i]);
  }

  *returnSize = current_size;
  return target_array;
}
