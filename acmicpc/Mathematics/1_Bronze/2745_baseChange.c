#include <stdio.h>
#include <string.h>

int main()

{
    char str[100] = {0, };
    int i;
    int len;
    int temp;
    long long sum = 0;

    scanf("%s %d", str, &i);
    for (len = 0; str[len]; len++)
    {
        if (str[len] > '9')
           temp = str[len] - 'A' + 10;
        else
            temp = str[len] - '0';
        sum = sum*i + temp;
    }
    printf("%lld", sum);
}