#include <stdio.h>

int main()

{
    int i;
    int j;

    scanf("%d %d", &i, &j);
    printf("%d\n%d\n%d\n%d\n%d", i+j, i-j, i*j, i/j, i%j);
}