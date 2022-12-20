#include <stdio.h>

int main()
{
	long long i, j;
	long long k;
	scanf("%lld %lld", &i, &j);
	k = i - j;
	if (k < 0)
		k = -k;
	printf("%lld", k);
	return 0;	
}