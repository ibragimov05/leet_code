#include <stdbool.h>
#include <string.h>

bool detectCapitalUse(char *word)
{
  int word_len = strlen(word);
  if (word_len == 1)
    return true;

  bool all_capital = true;
  bool all_not_capital = true;
  bool is_first_capital = true;

  for (int i = 0; i < word_len; i++)
  {
    if (!(word[i] >= 65 && 90 >= word[i]))
    {
      all_capital = false;
    }

    if (!(word[i] >= 97 && 122 >= word[i]))
    {
      all_not_capital = false;
    }
  }

  if (all_capital || all_not_capital)
    return true;

  if (word[0] >= 65 && 90 >= word[0])
  {
    for (int i = 1; i < word_len; i++)
    {
      if (!(word[i] >= 97 && 122 >= word[i]))
      {
        return false;
      }
    }
    return true;
  }

  return false;
}
