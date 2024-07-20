#include <stdio.h>

int main()
{
    int x, y;
    
    scanf("%d %d", &x, &y);
    if (x > 0 && y > 0)
        printf("%d", 1);
    else if (x > 0 && y < 0)
        printf("%d", 4);
    else if (x < 0 && y < 0)
        printf("%d", 3);
    else if (x < 0 && y > 0)
        printf("%d", 2);
    return 0;
}