#include <stdlib.h>
#include <stdio.h>

int main()
{
    int i;
    char c;
    
    scanf("%d", &i);
    c = 'F' - ((i - 40)/10);
    if (i < 60)
        c = 'F';
    if (i == 100)
        c = 'A';
    printf("%c", c);
}