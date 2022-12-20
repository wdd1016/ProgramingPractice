#include <stdio.h>
#include <unistd.h>

int main()
{
    int i, j, k;
    scanf("%d", &i);
    for (j=0; j<i; j++)
    {
        for (k=0; k<=j; k++)
            printf("%c", '*');
        printf("\n");
    }
    return 0;
}