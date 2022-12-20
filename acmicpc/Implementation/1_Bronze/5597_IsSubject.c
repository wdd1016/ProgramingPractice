#include <stdio.h>

int main()
{
    int a[28] = {};
    int i = 0;
    int j = 1;
    
    for (i=0; i<28; i++)
    {
        scanf("%d", &a[i]);
    }
    for (j=1; j<=30; j++)
    {
        for (i=0; i<28; i++)
         {
            if (a[i] == j)
                break;
            if (i == 27)
                printf("%d\n", j);
         }
    }
    return 0;
}