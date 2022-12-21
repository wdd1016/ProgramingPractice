#include <stdio.h>

int main()
{

    int i;
    int j;
    int min = 1000000;
    int max = -1000000;

    scanf("%d", &i);
    int arr[i];
    for (j=0; j<i; j++)
        scanf("%d", &arr[j]);
    for (j=0; j<i; j++)
    {
        if (arr[j] < min)
            min = arr[j];
        if (arr[j] > max)
            max = arr[j];
    }
    printf("%d %d", min, max);
    return 0;
}