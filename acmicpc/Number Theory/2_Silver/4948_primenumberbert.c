#include <stdio.h>
#include <stdlib.h>

int	ft_is_prime_num(int nb);

int main()
{
	int i;

	while (1)
	{
		scanf("%d", &i);
		int count = 0;
		if (i == 0)
			break;
		for (int k = i+1 ; k <= 2*i; k++)
		{
			if (ft_is_prime_num(k))
				count++;
		}
		printf("%d\n", count);
	}
	return 0;
}

int	ft_is_prime_num(int nb)
{
	int	i;

	if (nb <= 1)
		return (0);
	if (nb <= 3)
		return (1);
	if (nb % 2 == 0 || nb % 3 == 0)
		return (0);
	i = 2;
	while (i <= nb / i)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}