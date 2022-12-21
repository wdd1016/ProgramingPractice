#include <stdio.h>
#include <stdlib.h>

int main()
{
	int	i;
	char *str;
	
	scanf("%d", &i);
	str = (char *)malloc(sizeof(char) * (i + 1));
	str[i] = '\0';
	for (int j = i - 1; j >= 0; j--) // j는 공백개수
	{
		for (int k = 0; k < i; k++)
		{
			if (k < j) // 인덱스가 0 ~ j-1 일때는 공백
				str[k] = ' ';
			else
				str[k] = '*';
		}
		printf("%s\n", str);
	}
	return 0;
}