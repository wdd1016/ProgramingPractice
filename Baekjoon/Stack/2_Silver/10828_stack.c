#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 10000

typedef struct s_stack
{
	int	data[MAXSIZE];
	int	front;
	int	rear;
}	t_stack;

int ft_isempty(t_stack *stk)
{
	if (stk->front == stk->rear)
		return 1;
	else
		return 0;
}

void ft_push(t_stack *stk, char *str)
{
	(stk->data)[stk->front] = atoi(str);
	stk->front = (stk->front - 1 + MAXSIZE) % MAXSIZE;
}

int ft_pop(t_stack *stk)
{
	if (ft_isempty(stk) == 1)
		return -1;
	stk->front = (stk->front + 1) % MAXSIZE;
	return ((stk->data)[stk->front]);
}

int ft_size(t_stack *stk)
{
	return ((stk->rear - stk->front + MAXSIZE) % MAXSIZE);
}

int ft_top(t_stack *stk)
{
	if (ft_isempty(stk) == 1)
		return -1;
	return((stk->data)[(stk->front + 1) % MAXSIZE]);
}

int main()
{
	int n, len;
	char str[10] = { 0, };
	t_stack stack;

	scanf("%d", &n);
	stack.front = 0;
	stack.rear = 0;
	for (int i = 0; i < n; i++)
	{
		scanf("%s", str);
		len = strlen(str);
		if (len == 3)
		{
			if (str[0] == 't')
				printf("%d\n", ft_top(&stack));
			else
				printf("%d\n", ft_pop(&stack));
		}
		else if (len == 4)
		{
			if (str[0] == 'p')
			{
				scanf("%s", str);
				ft_push(&stack, str);
			}
			else
				printf("%d\n", ft_size(&stack));
		}
		else
			printf("%d\n", ft_isempty(&stack));
	}
}
