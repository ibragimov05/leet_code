#include <string.h>

char *firstPalindrome(char **words, int wordsSize)
{
  for (int i = 0; i < wordsSize; i++)
  {
    int is_palindrome = 0;
    int word_len = strlen(words[i]);

    for (int j = 0; j < word_len / 2; j++)
    {
      if (words[i][j] != words[i][word_len - j - 1])
      {
        is_palindrome = 1;
        break;
      }
    }

    if (!is_palindrome)
    {
      return words[i];
    }
  }

  return "";
}
