#include <stdio.h>
#include <stdlib.h>

int main()
{
	char str[101];

	while (scanf("%[^\n]s", str) != EOF)
	{
		getchar();
		printf("%s\n", str);
	}
	return 0;
}