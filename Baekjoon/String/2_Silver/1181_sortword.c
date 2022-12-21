#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compareal(const void *fir, const void *sec)
{
	return (strcmp((*(char **)fir), (*(char **)sec)));
}
int comparelen(const void *fir, const void *sec)
{
	return (strlen((*(char **)fir)) - strlen((*(char **)sec)));
}

int main()
{
	int i, n, j;

	scanf("%d", &n);
	char **str;
	str = (char **)malloc(sizeof(char *) * n);
	for (i=0; i<n; i++)
	{
		str[i] = (char *)malloc(sizeof(char) * 51);
	}
	for (i=0; i<n; i++)
	{
		scanf("%s", str[i]);
		for (j=0; j<i; j++)
		{
			if (strcmp(str[j], str[i]) == 0)
			{
				str[i][0] = '\0';
				break;
			}
		}
	}
	qsort(str, n, sizeof(char **), compareal);
	qsort(str, n, sizeof(char **), comparelen);
	for (i=0; i<n; i++)
	{
		if (str[i][0] != '\0')
			printf("%s\n", str[i]);
	}
	return 0;
}

// qsort https://kldp.org/node/157287