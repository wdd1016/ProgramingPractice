#include <stdio.h>

int main()
{
    int i;
    scanf("%d", &i);
    if (i % 4 == 0)
    {
        if (i % 100 == 0 && i % 400 != 0)
        {
            printf("%d", 0);
            return 0;
        }
        printf("%d", 1);
    }
    else
        printf("%d", 0);
    return 0;
}