#include <stdio.h>
#include <stdlib.h>

int main()
{
	int	i = 1;
	int j = 1;
	
	while (i || j)
	{
		scanf("%d %d", &i, &j);
		if (i || j)
			printf("%d\n", i + j);
	}
	return 0;
}