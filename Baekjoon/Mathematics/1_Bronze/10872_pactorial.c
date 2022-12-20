#include <stdio.h>

int ft(int i)
{
    if (i == 0)
        return 1;
    else
        return (i * ft(i - 1));
}

int main()
{
    int i;
    
    scanf("%d", &i);
    printf("%d", ft(i));
}