#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

/*
 * This algorithm is optimal in space.
 * The main idea is to find if s[i] (current character) is a duplicate.
 * t marks the duplicate charater. If the s[i] is not a duplicate t
 * will be increasing with i. If i is a duplicate, t will point to i
 * and i will increase. If the new character is not a duplicate, we will
 * move it to the left. If you have an stretch of repeats, t will point
 * to the first repeat, and, when leaving the main loop, we will set
 * the end of the string in s[t] (aaaa -> a)
 * Fascinating.
 */
void _remove(char *s) {
  int i, j, t, len;
  len = strlen(s);

  t = 1;
  for (i=1; i<len; ++i) {
    for (j=0; j<t; ++j)
      if (s[j] == s[i]) break;

    if (j == t) {
      s[t] = s[i];
      ++t;
    }
  }
  s[t] = '\0';
}

void check(char *o, char *r) {
  char *s2;
  s2 = malloc(strlen(o) + 1);
  strcpy(s2, o);
  _remove(s2);
  printf("I:%s T:%s C:%s\n", o, r, s2);
  assert(strcmp(s2, r) == 0);
}

int main(int argc, char **argv) {
  check("AbcAd", "Abcd");
  check("aaaa", "a");
  check("", "");
  check("aaabbb", "ab");
  check("David", "David");
  return 0;
}
