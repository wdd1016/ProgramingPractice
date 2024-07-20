#include <stdio.h>
#include <math.h>

typedef struct s_coor
{
	int row;
	int col;
}	t_coor;

void ft_find_count(t_coor start, int length, \
int number, t_coor goal)
{
	if (length == 1)
	{
		if (start.row == goal.row && start.col == goal.col)
			printf("%d", number);
	}
	else
	{
		length /= 2;
		if (start.row + length > goal.row) // 4분면에서 북서쪽, 북동쪽에 정답 위치
		{
			if (start.col + length > goal.col) // 북서쪽
			{
				ft_find_count(start, length, number, goal);
			}
			else // 북동쪽
			{
				start.col += length;
				number += length * length;
				ft_find_count(start, length, number, goal);
			}
		}
		else // 4분면에서 남서쪽, 남동쪽
		{
			if (start.col + length > goal.col) // 남서쪽
			{
				start.row += length;
				number += length * length * 2;
				ft_find_count(start, length, number, goal);
			}
			else // 남동쪽
			{
				start.row += length;
				start.col += length;
				number += length * length * 3;
				ft_find_count(start, length, number, goal);
			}
		}
	}
}

int main()
{
	int n, r, c;
	t_coor start = {0, 0};

	scanf("%d %d %d", &n, &r, &c);
	int length = pow(2, n);
	t_coor goal = {r, c};
	ft_find_count(start, length, 0, goal);
	return 0;
}