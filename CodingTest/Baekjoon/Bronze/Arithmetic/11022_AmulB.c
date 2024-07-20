#include <stdio.h>
#include <stdlib.h>

int main()
{
	int	i;
	int j, k;
	
	scanf("%d", &i);
	for (int l = 0; l < i; l++)
	{
		scanf("%d %d", &j, &k);
		printf("Case #%d: %d + %d = %d\n", l + 1, j, k, k + j);
	}
	return 0;
}