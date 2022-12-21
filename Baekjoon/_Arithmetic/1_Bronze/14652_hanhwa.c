#include <stdio.h>

int main()
{
	int k, n, m;
	int x, y;
	scanf("%d %d %d", &n, &m, &k);
	x = k / m;
	y = k % m;
	printf("%d %d", x, y);
}