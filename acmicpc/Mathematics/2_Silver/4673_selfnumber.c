#include <stdio.h>
#include <math.h>

int main()
{
    int i;
    int j;
    int k;
    int sum;
    
    for (i=1; i<=10000; i++)
    {
        j = i - (9 * ((int)log10(i) + 1));
        if ( j < 1 )
            j = 1;
        for (; j <= i; j++)
        {
            sum = j;
            for (k=j; k>0; k/=10)
            {
                sum += k % 10;
            }
            if (sum == i)
                break;
            else if (j == i)
                printf("%d\n", i);
        }
    }
}