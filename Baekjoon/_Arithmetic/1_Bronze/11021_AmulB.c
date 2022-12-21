#include <stdio.h>

int main()
{
    int i;
    int j, k, l;

    scanf("%d", &i);
    for (l=1; l<=i; l++)
    {
        scanf("%d %d", &j, &k);
        printf("Case #%d: %d\n", l, k+j);
    }  
}