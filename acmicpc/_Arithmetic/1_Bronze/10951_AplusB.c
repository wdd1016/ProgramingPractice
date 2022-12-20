#include <stdio.h>
#include <stdlib.h>

int main()
{
	int	i = 1;
	int j = 1;
	
	while (scanf("%d %d", &i, &j) != EOF)
	{
		printf("%d\n", i + j);
	}
	return 0;
}