#include <iostream>

using namespace std;
int main() {

	int n, k;
	cin >> n >> k;

	int arr[n][n];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	int ansarr[9] = {0, };
	int tmp;
	for (int i = 0; i < n; i++) {
		for  (int j = 0; j < n; j++) {
			if (arr[i][j] == 1)
				continue;
			tmp = 0;
			for (int a = i - 1; a <= i + 1; a++) {
				if (a < 0 || a >= n)
					continue;
				for (int b = j - 1; b <= j + 1; b++) {
					if (b < 0 || b >= n)
						continue;
					else if (arr[a][b] == 1)
						tmp++;
				}
			}
			ansarr[tmp]++;
		}
	}
	cout << ansarr[k] << endl;
	return 0;
}
