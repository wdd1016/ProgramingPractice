#include <stdio.h>

int main()
{
    int i;
    int j;
    
    scanf("%d %d", &i, &j);
    printf("%d\n%d\n%d\n%d", i*(j%10), i*((j%100)/10), i*(j/100), i*j);
}