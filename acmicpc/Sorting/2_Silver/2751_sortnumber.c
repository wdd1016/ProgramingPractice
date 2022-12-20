#include <stdio.h>
#include <stdlib.h>

static int compare(const void *fir, const void *sec)
{
    if (*((int *)fir) > *((int *)sec))
       return 1;
    else if (*((int *)fir) > *((int *)sec))
       return -1;
    else
       return 0;
}

int main()
{
    int i, j;
    int *arr;

    scanf("%d", &i);
    arr = (int *)malloc(sizeof(int) * i);
    for (j=0; j<i; j++)
    {
        scanf("%d", &(arr[j]));
    }
    qsort(arr, i, sizeof(int), compare);
    for (j=0; j<i; j++)
    {
        printf("%d\n", arr[j]);
    }
    return 0;
}