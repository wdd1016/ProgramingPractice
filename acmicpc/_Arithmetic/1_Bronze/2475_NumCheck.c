#include <stdio.h>
#include <stdlib.h>

int main()
{
	int num;
	int	sum = 0;

	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &num);
		sum += num * num;
	}
	printf("%d", sum % 10);
}