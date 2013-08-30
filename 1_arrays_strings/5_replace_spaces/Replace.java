public class Replace {
  private static void _replace(char []s, int length) {
    int n_spaces = 0,
        j = 0;

    for (int i=0; i<length; ++i)
      if (s[i] == ' ') ++n_spaces;

    j = length + (n_spaces * 2);
    s[j] = '\0';

    for (int i=length; i>=0; --i) {
      if (s[i] == ' ') {
        s[j]   = '0';
        s[j-1] = '2';
        s[j-2] = '%';
        j = j-3;
      }
      else {
        s[j] = s[i];
        j = j - 1;
      }
    }
  }

  private static void check(String is, String t) {
    char[] ca  = new char[1000];
    char[] tca = new char[1000];
    int i;
    for (i = 0; i < is.length(); ++i) ca[i] = is.charAt(i);
    ca[i] = '\0';
    for (i = 0; i < t.length(); ++i) tca[i] = t.charAt(i);
    tca[i] = '\0';

    _replace(ca, is.length());
    String result = new String(ca);
    String ts = new String(tca);
    System.out.format("I:%s T:%s R:%s (%d|%d)\n", is, ts, result, ts.length(), result.length());
    assert ts.equals(result);
  }

  public static void main(String[] args) {
    check("Hello", "Hello");
    check("Foo ", "Foo%20");
    check(" X ", "%20X%20");
  }
}
