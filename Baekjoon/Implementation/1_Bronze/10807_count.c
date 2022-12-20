#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i, k;
	int count = 0;

	scanf("%d", &i);
	int arr[i];
	for (int j = 0; j < i; j++)
	{
		scanf("%d", &arr[j]);
	}
	scanf("%d", &k);
	for (int j = 0; j < i; j++)
	{
		if (arr[j] == k)
			count++;
	}
	printf("%d", count);
	return 0;
}