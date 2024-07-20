#include <stdio.h>

int main()
{
	int n;
	int m;
	int i, j, k;
	int	max, temp;

	scanf("%d %d", &n, &m);
	int arr[n];
	for (i=0; i<n; i++)
	{
		scanf("%d", &(arr[i]));
	}
	max = 0;
	for (i=0; i<n-2; i++)
	{
		for (j=i+1; j<n-1; j++)
		{
			for (k=j+1; k<n; k++)
			{
				temp = arr[i] + arr[j] + arr[k];
				if (temp > max && temp <= m)
					max = temp;
				if (max == m)
				{
					printf("%d", m);
					return 0;
				}
			}
		}
	}
	printf("%d", max);
	return 0;
}