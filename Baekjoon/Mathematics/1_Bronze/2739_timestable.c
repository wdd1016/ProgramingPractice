#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int i;

	scanf("%d", &i);
	for (int j = 1; j < 10; j++)
	{
		printf ("%d * %d = %d\n", i, j, i*j);
	}
	return 0;
}