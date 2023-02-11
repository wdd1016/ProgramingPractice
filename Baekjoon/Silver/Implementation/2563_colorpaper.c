#include <stdio.h>

int main()
{
	int i, j, k, m, row, col;
	int sum = 0;
	int arr[100][100] = {0, };

	scanf("%d", &i);
	for (j=0; j<i; j++)
	{
		scanf("%d %d", &col, &row);
		for (k=0; k<10; k++)
		{
			for (m=0; m<10; m++)
			{
				arr[row+k][col+m] = 1;
			}
		}
	}
	for (j=0; j<100; j++)
	{
		for (k=0; k<100; k++)
		{
			if (arr[j][k] == 1)
				sum++;
		}
	}
	printf("%d", sum);
}