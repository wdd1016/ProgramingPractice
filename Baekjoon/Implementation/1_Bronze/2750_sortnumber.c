#include <stdio.h>
#include <stdlib.h>

int compare(const void *fir, const void *sec)
{
    return(*(int *)fir - *(int *)sec);
}

int main()
{
    int n;
    int i;

    scanf("%d", &n);
    int arr[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), compare);
    for (i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
    }
}