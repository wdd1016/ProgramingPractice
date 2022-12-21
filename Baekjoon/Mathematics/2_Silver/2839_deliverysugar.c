#include <stdio.h>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int ft_count(int nbr, int *arr)
{
    int three;
    int five;
    
    if (nbr == 3 || nbr == 5)
        return (1);
    else if (nbr < 5)
        return (-1);
    else if (arr[nbr] == 0)
    {
        three = ft_count(nbr-3, arr);
        five = ft_count(nbr-5, arr);
        if (three == -1 && five == -1)
            arr[nbr] = -1;
        else if (three == -1)
            arr[nbr] = 1 + five;
        else if (five == -1)
            arr[nbr] = 1 + three;
        else
            arr[nbr] = 1 + MIN(three, five);
    }
    return arr[nbr];
}

int main()
{
    int i;
    int arr[5001] = { 0, };
    
    scanf("%d", &i);
    printf("%d", ft_count(i, arr));
}