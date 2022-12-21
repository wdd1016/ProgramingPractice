#include <stdio.h>

int ft_num(int num)
    {
    if (num == 1)
        return 0;
    else if (num <= 3)
        return 1;
    else if ((num % 2 == 0) || (num % 3 == 0))
        return 0;
    for (int i = 2; i <= num / i; i++)
        {
        if (num % i == 0)
            return 0;
    }
    return 1;
}

int main()
{
    int i;
    int j;
    int count = 0;

    scanf("%d", &i);
    for (; i>0; i--)
        {
        scanf("%d", &j);
        if (ft_num(j))
            count++;
    }
    printf("%d", count);
    return 0;
}