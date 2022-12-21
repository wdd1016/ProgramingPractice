#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
	int		i;
	int		j;
	char	*str;
	int left = 0;
	int right = 0;
	int count = 0;

	scanf("%d", &i);
	str = (char *)malloc(sizeof(char) * (i + 1));
	for (j=0; j<i; j++)
	{
		scanf(" %c", &str[j]); // 배열생성
		if (str[j] == '(')
			left++;
		else
			right++;
	}
	if (left != right) // 맞지않으면 에러
	{
		printf("%d", -1);
		return 0;		
	}
	left = 0;
	right = 0;
	str[i] = 0;
	for (j=0; j<i; j++)
	{
		if (str[j] == '(')
			left++;
		else
			right++;
		if (abs(left - right) > count)
			count = abs(left - right);
	}
	printf("%d", count);
}

// test 32 (((((((((((()))((())))))()))))))
// test 28 )))((()()(((()))()))((()(())
// test 32 )))((()()(((((()))()))((()(())))