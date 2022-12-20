#include <stdio.h>

int main()
    {
    int sum = 0;
    int i, j;
    
    scanf("%d", &i);
    for (j=1; j<=i; j++)
        {
        sum += j;
    }
    printf("%d", sum);
    
}