#include <stdio.h>

int main()
{
    int i, j, k, l;
    scanf("%d", &i);
    for (j=0; j<i; j++)
    {
        scanf("%d %d", &k, &l);
        printf("%d\n", k+l);
    }
}