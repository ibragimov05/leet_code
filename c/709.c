#include <string.h>

char *toLowerCase(char *s)
{
  int s_len = strlen(s);
  char *word = (char *)malloc((s_len + 1) * sizeof(char));

  if (word == NULL)
    return NULL;

  for (int i = 0; i < s_len; i++)
  {
    int ascii_value = (int)s[i];

    if (ascii_value >= 65 && 90 >= ascii_value)
    {
      word[i] = (char)ascii_value + 32;
    }
    else
    {
      word[i] = (char)ascii_value;
    }
  }

  word[s_len] = '\0';
  return word;
}
