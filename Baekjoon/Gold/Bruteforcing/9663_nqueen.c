#include <stdio.h>

int	ft_is_valid_place(int *queen, int index)
{
	int	i;

	i = 0;
	while (i < index)
	{
		if (queen[i] == queen[index])
			return (0);
		if (queen[i] - (index - i) == queen[index])
			return (0);
		if (queen[i] + (index - i) == queen[index])
			return (0);
		i++;
	}
	return (1);
}

void	ft_queens_write(int *queen, int *count, int index, int max)
{
	int	i;

	i = 0;
	while (i < max)
	{
		queen[index] = i;
		if (ft_is_valid_place(queen, index) == 1)
		{
			if (index == max - 1)
				(*count)++;
			else
				ft_queens_write(queen, count, index + 1, max);
		}
		i++;
	}
}

int	main(void)
{
	int	count = 0;
	int i;

	scanf("%d", &i);
	int	queen[i];
	ft_queens_write(queen, &count, 0, i);
	printf("%d", count);
}
