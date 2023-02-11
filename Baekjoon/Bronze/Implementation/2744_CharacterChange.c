#include <stdio.h>

int main()

{
    char str[101];

    scanf("%s", str);
    for (int i = 0; str[i]; i++)
    {
        if (str[i] >= 'a')
            str[i] -= 32;
        else
            str[i] += 32;
    }
    printf("%s", str);
}