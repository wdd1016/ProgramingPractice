#include <stdio.h>
#include <stdlib.h>

int main()
{
	char str[101];
	int i;

	scanf("%s", str);
	for (i = 0; str[i]; i++);
	printf("%d", i);
	return 0;
}