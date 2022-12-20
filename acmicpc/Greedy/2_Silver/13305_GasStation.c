#include <stdio.h>
#include <stdlib.h>

void ft_max_cost(int *price, int *distance, int max, unsigned long long *cost)
{
    int i;
    int temp_price_min;
    unsigned long long dis_sum = 0;
    
    temp_price_min = price[0];
    for (i = 0; i <= max; i++)
    {
        if (price[i] < temp_price_min || i == max)
        {
            *cost += (unsigned long long)temp_price_min * dis_sum;
            temp_price_min = price[i];
            dis_sum = 0;
        }
        dis_sum += distance[i];
    }
}

int main()
{
    int *price;
    int *distance;
    int i;
    int j;
    int max = 0;
    unsigned long long cost = 0;
    
    scanf("%d", &i);
    price = (int *)malloc(sizeof(int) * i);
    distance = (int *)malloc(sizeof(int) * (i - 1));
    for (j = 0; j < i - 1; j++)
    {
        scanf("%d", &distance[j]);
    }
    for (j = 0; j < i; j++)
    {
        scanf("%d", &price[j]);
    }
    max = i - 1;
    ft_max_cost(price, distance, max, &cost);
    printf("%llu", cost);
}