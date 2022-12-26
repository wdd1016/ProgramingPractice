#include <stdio.h>
#include <string.h>

# define DOT '.'
# define VER '|'
# define HOR '-'
# define ALL '+'

int ft_isright(int size, int row, int col, char order)
{
	switch (order) {
		case 'U':
			row--;
			break;
		case 'D':
			row++;
			break;
		case 'L':
			col--;
			break;
		case 'R':
			col++;
			break;
		default:
			break;
	}
	if (row >= 0 && row < size && col >= 0 && col < size)
		return 1;
	else
		return 0;
}

void ft_draw_line(char *dot, char order)
{
	if (order == 'U' || order == 'D')
	{
		if (*dot == DOT)
			*dot = VER;
		else if (*dot == HOR)
			*dot = ALL;
	}
	else if (order == 'L' || order == 'R')
	{
		if (*dot == DOT)
			*dot = HOR;
		else if (*dot == VER)
			*dot = ALL;
	}
}

void ft_move_matrix(int order, int *row, int *col)
{
	switch (order) {
		case 'U':
			(*row)--;
			break;
		case 'D':
			(*row)++;
			break;
		case 'L':
			(*col)--;
			break;
		case 'R':
			(*col)++;
			break;
		default:
			break;
	}
}

int main()
{
	int 	size;
	char	str[251];
	int		len;
	int		row;
	int		col;

	scanf("%d", &size);
	char	wood[size][size];

	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
			wood[row][col] = DOT;
	}
	row = 0;
	col = 0;
	scanf("%s", str);
	len = strlen(str);
	for (int k = 0; k < len; k++)
	{
		if (ft_isright(size, row, col, str[k]))
		{
			ft_draw_line(&(wood[row][col]), str[k]);
			ft_move_matrix(str[k], &row, &col);
			ft_draw_line(&(wood[row][col]), str[k]);
		}
	}
	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
			printf("%c", wood[row][col]);
		printf("\n");
	}
	return 0;
}
