#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void	ft_pow_2_big_int(char *num, int multiple)
{
	int	j;
	int	k;
	int mul;
	int temp;

	for (j=0; j<multiple; j++)
	{
		for (k=0; k<30; k++)
		{
			temp = 2 * (num[k] - '0') + ((num[k+1] - '0') * 2 / 10);
			temp %= 10;
			num[k] = temp + '0';
		}
		temp = 2 * (num[k] - '0');
		temp %= 10;
		num[k] = temp + '0';
	}
	num[30] -= 1;
	for (j=0; num[j] == '0'; j++);
	printf("%s\n", num + j);
}

void	ft_hanoi(int i, int start, int end, int sub)
{
	if (i == 1)
	{
		printf("%d %d\n", start, end);
		return;
	}
	else
	{
		ft_hanoi(i - 1, start, sub, end);
		printf("%d %d\n", start, end);
		ft_hanoi(i - 1, sub, end, start);
	}
}

int main()
{
	int	i;
	char num[32];

	for (i=0; i<30; i++)
		num[i] = '0';
	num[31] = '\0';
	num[30] = '1';
	scanf("%d", &i);
	ft_pow_2_big_int(num, i);
	if (i <= 20)
	{
		ft_hanoi(i, 1, 3, 2);
	}
	return 0;
}