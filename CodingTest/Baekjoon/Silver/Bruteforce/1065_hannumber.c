#include <stdio.h>

int main()
{
    int i, j, k, l, m;
    int temp;
    int count = 0;

    scanf("%d", &i);
    if (i < 100)
    {
        printf("%d", i);
        return 0;
    }
    else
    {
        if (i == 1000)
            i = 999;
        for (j = 100; j <= i; j++)
        {
            k = (j / 100) % 10;
            l = (j / 10) % 10;
            m = j % 10;
            if ((k - l) == (l - m))
                count++;
        }
        printf("%d", count + 99);
        return 0;
    }
}

