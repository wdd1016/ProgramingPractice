#include <stdio.h>
#include <string.h>
int main()

{

    char i[60];
    char *j = "??!";

    scanf("%s", i);
    printf("%s", strcat(i, j));

}