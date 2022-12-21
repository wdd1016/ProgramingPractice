#include <stdlib.h>
#include <stdio.h>

typedef struct s_coor
{
    int x;
    int y;
}    t_coor;

int	compare(const void *fir, const void *sec)
{
	if (((t_coor *)fir)->x > ((t_coor *)sec)->x)
		return 1;
	else if (((t_coor *)fir)->x < ((t_coor *)sec)->x)
		return -1;
	else if (((t_coor *)fir)->x == ((t_coor *)sec)->x)
	{
		if (((t_coor *)fir)->y > ((t_coor *)sec)->y)
			return 1;
		else if (((t_coor *)fir)->y < ((t_coor *)sec)->y)
			return -1;
		else
			return 0;
	}
	else
		return 0;
}

int main()
{
    int n;
    int i;
    t_coor *spot;
    
    scanf("%d", &n);
    spot = (t_coor *)malloc(sizeof(t_coor) * n);
    for (i=0; i<n; i++)
    {
        scanf("%d %d", &(spot[i].x), &(spot[i].y));
    }
	qsort(spot, n, sizeof(t_coor), compare);
	for (i=0; i<n; i++)
	{
		printf("%d %d\n", spot[i].x, spot[i].y);
	}
}