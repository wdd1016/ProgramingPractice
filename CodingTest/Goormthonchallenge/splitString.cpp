#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;


int main() {
	int n;

	cin >> n;
	string str;

  cin >> str;
  vector<string> vtr;

  int start = 0;
  int len = 1;
  int num = 0;
  int strlen = str.length();
  int maxlen = strlen - 2;

	while (true) {
    if (find(vtr.begin(), vtr.end(), str.substr(start, len)) == vtr.end())
      vtr.push_back(str.substr(start, len));
    len++;
    if (len > maxlen) {
      start++;
      if (start == strlen)
        break;
      if (start == 1)
        maxlen = strlen - 2;
      else
        maxlen = strlen - start;
      len = 1;
    }
	}
  sort(vtr.begin(), vtr.end(), [](string a, string b) {
    return a < b;
  });

  int max = 0;
  int tmp;

  int fir = 0;
  for (int sec = fir + 1; sec < strlen - 1; sec++) {
    for (int thir = sec + 1; thir < strlen; thir++) {
      tmp = find(vtr.begin(), vtr.end(), str.substr(fir, sec - fir)) - vtr.begin() + 1
      + find(vtr.begin(), vtr.end(), str.substr(sec, thir - sec)) - vtr.begin() + 1
      + find(vtr.begin(), vtr.end(), str.substr(thir, strlen - thir)) - vtr.begin() + 1;
      if (tmp > max)
        max = tmp;
    }
  }

	cout << max << endl;
	return 0;
}