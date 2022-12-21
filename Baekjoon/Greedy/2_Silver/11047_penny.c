#include <stdio.h>

int main()
    {
    int n, k, i;
    int count = 0;
    scanf("%d %d", &n, &k);
    int arr[n];
    for (i=0; i<n; i++)
    {
        scanf("%d", &(arr[i]));
    }
    while (k >= arr[n-1])
    {
        k -= arr[n-1];
        count++;
    }
    while (k > 0)
    {
        for (i=0; i<n; i++)
        {
            if (arr[i] == k)
            {
                k -= arr[i];
                count++;
                break;
            }
            else if (arr[i] > k)
            {
                k -= arr[i-1];
                count++;
                break;
            }
        }
    }
    printf("%d", count);
}