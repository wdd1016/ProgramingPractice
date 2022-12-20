#include <stdio.h>

int main()
{
    int i, j, k;
    
    scanf("%d %d", &i, &j);
    int arr[i];
    for (k=0; k<i; k++)
    {
        scanf("%d", &(arr[k])); 
    }
    for (k=0; k<i; k++)
    {
        if (arr[k] < j)
            printf("%d ", arr[k]);
    }
    return 0;
}