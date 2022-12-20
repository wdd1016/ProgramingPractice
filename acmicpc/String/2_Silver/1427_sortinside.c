#include <stdio.h>
#include <stdlib.h>

int cmp(const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return -1;
    else if (*(int*)first < *(int*)second)
        return 1;
    else
        return 0;
}


int main()
{
    int i, temp;
    int len = 0;
    int arr[10];
    scanf("%d", &i);
    temp = i;
    while (temp > 0)
    {
        arr[len] = temp % 10;
        temp /= 10;
        len++;
    }
    qsort(arr, len, sizeof(int), cmp);
    for (temp=0; temp<len; temp++)
        printf("%d", arr[temp]);
    return 0;
}