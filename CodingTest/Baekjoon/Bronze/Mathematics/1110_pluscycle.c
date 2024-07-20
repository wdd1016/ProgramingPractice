#include <stdlib.h>
#include <stdio.h>

int main()
{
    int i, temp;
    int count = 0;
    
    scanf("%d", &i);
    temp = i;
    do
    {
        if (temp < 10)
        {
            temp *= 11;
        }
        else
            temp = (temp % 10) * 10 + (temp / 10 + temp % 10) % 10;
        count++;
    } while (temp != i);
    printf("%d", count);
    return 0;
}
