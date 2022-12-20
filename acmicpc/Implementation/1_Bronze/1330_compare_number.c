#include <stdio.h>

int main()
{
    int i;
    int j;
    
    scanf("%d", &i);
    scanf("%d", &j);
    if (i < j)
        printf("%s", "<");
    else if (i > j)
        printf("%s", ">");
    else
        printf("%s", "==");
    return 0;
}