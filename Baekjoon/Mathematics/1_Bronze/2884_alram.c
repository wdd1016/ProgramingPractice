#include <stdio.h>

int main()
{
    int min, sec;
    
    scanf("%d %d", min, sec);
    if (sec >= 45)
    {
        sec -= 45;
        printf("%d %d", min, sec);
        return 0;
    }
    else
    {
        if (min == 0)
        {
            min = 23;
            sec += 15;
            printf("%d %d", min, sec);
            return 0;
        }
        else
        {
            min -= 1;
            sec += 15;
            printf("%d %d", min, sec);
            return 0;
        }
    }
}