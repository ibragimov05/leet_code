#include <stdbool.h>
#include <string.h>

char *reversePrefix(char *word, char ch)
{
  bool contain = false;
  int prefix_index;

  for (int i = 0; i < strlen(word); i++)
  {
    if (word[i] == ch)
    {
      contain = true;
      prefix_index = i;
      break;
    }
  }

  if (!contain)
  {
    return word;
  }

  int l = 0;
  int r = prefix_index;
  char t;

  while (l < r)
  {
    t = word[l];
    word[l] = word[r];
    word[r] = t;

    l++;
    r--;
  }

  return word;
}
