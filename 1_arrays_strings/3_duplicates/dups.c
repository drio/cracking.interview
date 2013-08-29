#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void _remove(char *s) {
  int i, j, t, len;
  len = strlen(s);

  t = 1; // will point to duplicate indices
  for (i=1; i<len; ++i) { // screen the input string
    for (j=0; j<t; ++j)   // is there any duplicate for s[i] ?
      if (s[j] == s[i]) break; // !! s[j] is a duplicate of s[i] .. (*)

    if (j == t) { // t points to a duplicate,
      s[t] = s[i]; // shift
      ++t; // because of the shift, t+1 is a duplicate
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
