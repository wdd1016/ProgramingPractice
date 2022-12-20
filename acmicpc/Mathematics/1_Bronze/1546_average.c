#include <stdio.h>

int main()
{
    int i = 0;
    int j = 0;
    int max = 0;
    int sum = 0;
    
    scanf("%d", &i);
    int array[i];
    for (j = 0; j < i; j++)
    {
        scanf("%d", &array[j]);
    }
    for (j = 0; j < i; j++)
    {
       if(array[j] > max)
           max = array[j];
       sum += array[j];
    }
    printf("%f", (float)(sum*100) / (float)(max*i));
}
