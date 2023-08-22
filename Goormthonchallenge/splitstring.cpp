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
  map<string, int> locmap;

  int start = 0;
  int len = 1;
  int num = 0;
  int strlen = str.length();
  int maxlen = strlen - 2;

	while (true) {
    locmap[str.substr(start, len)] = ++num;
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

  int max = 0;
  int tmp;

  int fir = 0;
  for (int sec = fir + 1; sec < strlen - 1; sec++) {
    for (int thir = sec + 1; thir < strlen; thir++) {
      tmp = locmap[str.substr(fir, sec - fir)]
      + locmap[str.substr(sec, thir - sec)]
      + locmap[str.substr(thir, strlen - thir)];
      if (tmp > max)
        max = tmp;
    }
  }

	cout << max << endl;
	return 0;
}