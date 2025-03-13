#include <stdio.h>
#include <string.h>

int countMatches(char ***items, int itemsSize, int *itemsColSize, char *ruleKey, char *ruleValue)
{
  int index_number = -1;

  if (strcmp(ruleKey, "type") == 0)
  {
    index_number = 0;
  }
  else if (strcmp(ruleKey, "color") == 0)
  {
    index_number = 1;
  }
  else if (strcmp(ruleKey, "name") == 0)
  {
    index_number = 2;
  }

  int match_count = 0;

  for (int i = 0; i < itemsSize; i++)
  {
    if (strcmp(items[i][index_number], ruleValue) == 0)
    {
      match_count++;
    }
  }

  return match_count;
}
