#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int	i;
	char str[101];
	char *alphabet = "abcdefghijklmnopqrstuvwxyz";
	int	location[26];
	
	scanf("%s", str);
	while (*alphabet)
	{
		if (strchr(str, *alphabet))
			printf("%ld ", strchr(str, *alphabet) - str);
		else
			printf("%d ", -1);
		alphabet++;
	}
	return 0;
}