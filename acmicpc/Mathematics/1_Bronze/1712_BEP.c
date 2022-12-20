#include <stdio.h>

int main()
{
    int a[3] ={};
    int i;
    
    for (i=0; i<3; i++)
    {
        scanf("%d", &a[i]);
    }
    if (a[1] >= a[2])
    {
        printf("%d", -1);
        return 0;
    }
    printf("%d", (a[0]/(a[2]-a[1])) + 1);
    return 0;
}