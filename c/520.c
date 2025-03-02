#include <stdbool.h>
#include <string.h>

bool detectCapitalUse(char *word)
{
  bool all_capital = true;
  bool all_not_capital = true;
  bool is_first_capital = true;

  int word_len = strlen(word);

  for (int i = 0; i < word_len; i++)
  {
    int char_letter = (int)word[i];

    if (!(char_letter >= 65 && 90 >= char_letter))
    {
      all_capital = false;
    }

    if (!(char_letter >= 97 && 122 >= char_letter))
    {
      all_not_capital = false;
    }
  }

  if (all_capital || all_not_capital)
    return true;

  if ((int)word[0] >= 65 && 90 >= (int)word[0])
  {
    for (int i = 1; i < word_len; i++)
    {
      int char_letter = (int)word[i];
      if (!(char_letter >= 97 && 122 >= char_letter))
      {
        return false;
      }
    }
    return true;
  }

  return false;
}
