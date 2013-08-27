#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void reverse(char *s) {
  int i, j, tmp, len;
  len = strlen(s);
  for (i=0; i<len-1; i++) {
    j = len - i - 1;
    if (i >= len/2) break;
    tmp = s[i];
    s[i] = s[j];
    s[j] = tmp;
  }
}

void check(char *o, char *r) {
  char *s2;
  s2 = malloc(strlen(o) + 1);
  strcpy(s2, o);
  reverse(s2);
  assert(strcmp(s2, r) == 0);
}

int main(int argc, char **argv) {
  check("Foo", "ooF");
  check("casa", "asac");
  printf("OK\n");

  return 0;
}
