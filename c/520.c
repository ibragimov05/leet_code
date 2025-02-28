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

    if (char_letter >= 65 && 90 >= char_letter)
    {
    }
  }

  return all_capital || all_not_capital || is_first_capital;
}

// class Solution:
//     def detectCapitalUse(self, word: str) -> bool:
//         return word.upper() == word or word.capitalize() == word or word.lower() == word
