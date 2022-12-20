#include <stdio.h>
#include <math.h>

int ft_recursion(int a, int b, int c)
{
    if (a <= 0 || b <= 0 || c <= 0)
        return 1;
    else if (a > 20 || b > 20 || c > 20)
        return (1048576);
    else if (a == b && b == c)
        return ((int)pow(2, a));
    else if (c >= a)
        return ((int)pow(2, a));
    else if (a <= b && c < 20)
        return (ft_recursion(a, b, 20));
    else
        return (ft_recursion(a-1, b, c) + ft_recursion(a-1, b-1, c) + \
        ft_recursion(a-1, b, c-1) - ft_recursion(a-1, b-1, c-1));
}

int main()
{
    int arr[100000];
    int i = 0;
    while (1)
    {
        scanf("%d", &arr[i]);
        scanf("%d", &arr[i+1]);
        scanf("%d", &arr[i+2]);
        if (arr[i + 0] == -1 && arr[i + 1] == -1 && arr[i + 2] == -1)
            break;
        i += 3;
    }
    for (int k = 0; k < i; k += 3)
    {
        printf("w(%d, %d, %d) = ", arr[k + 0], arr[k + 1], arr[k + 2]);
        printf("%d\n", ft_recursion(arr[k + 0], arr[k + 1], arr[k + 2]));
    }
    return 0;
}