/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   2261_shortest_dis.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: juyojeon <juyojeon@student.42seoul.kr>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/21 18:22:38 by juyojeon          #+#    #+#             */
/*   Updated: 2022/11/21 23:43:31 by juyojeon         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))

typedef struct s_coor
{
    int x;
    int y;
}   t_coor;

int ft_dis_sqt(t_coor coor1, t_coor coor2)
{
    int x = coor1.x - coor2.x;
    int y = coor1.y - coor2.y;
    return (x*x + y*y);
}

int	compare_x(const void *fir, const void *sec)
{
	if (((t_coor *)fir)->x > ((t_coor *)sec)->x)
		return 1;
	else if (((t_coor *)fir)->x < ((t_coor *)sec)->x)
		return -1;
	else
		return 0;
}

int	compare_y(const void *fir, const void *sec)
{
	if (((t_coor *)fir)->y > ((t_coor *)sec)->y)
		return 1;
	else if (((t_coor *)fir)->y < ((t_coor *)sec)->y)
		return -1;
	else
		return 0;
}

int ft_try_all_coor_dis_return_short(t_coor *arr, int start, int end, int dis_sqt)
{
    int temp_sqt;
    int i;
    int j;

    for (i=start; i<end; i++)
    {
        for (j=i+1; j<=end; j++)
        {
            temp_sqt = ft_dis_sqt(arr[j], arr[i]);
            if (temp_sqt < dis_sqt)
            {
                dis_sqt = temp_sqt;
            }
        }
    }
    return (dis_sqt);
}

int ft_y_direction_min_sqt(t_coor *arr, int start, int end, int dis, int dis_sqt)
{
    int min;
    int max;
    int i;
    int len;
    int temp_sqt;
    t_coor *temp_arr;

    len = end - start + 1;
    temp_arr = (t_coor *)malloc(sizeof(t_coor) * len); // 스타트~엔드까지 x로 정렬된 배열을 하나 더생성
    for (i=0; i<len; i++)
    {
        temp_arr[i].x = arr[start + i].x;
        temp_arr[i].y = arr[start + i].y;
    }
    qsort(temp_arr, i, sizeof(t_coor), compare_y); // 임시배열을 y로 오름차순 정렬
    for (min = 0; min<len-1; min++)
    {
        for (max=min+1; max<len; max++)
        {
            if (temp_arr[max].y - temp_arr[min].y > dis)
                break;
        }
        temp_sqt = ft_try_all_coor_dis_return_short(temp_arr, min, max, dis_sqt);
        if (temp_sqt < dis_sqt)
        {
            dis_sqt = temp_sqt;
        }
    }
    free(temp_arr);
    return (dis_sqt);
}

int ft_min_dif(t_coor *arr, int start, int end, int mid_idx, int dis_sqt)
{
	int min; // dis 거리까지의 최소 인덱스
	int max; // dis 거리까지의 최대 인덱스
	int dis; // 1,2번의 최소 거리값(소수점 버림)
    int min_sqt_value; // 원하는 정답값 (비교후 제공, dis_sqt보다 모두 클경우 dis_sqt)

	dis = (int)sqrt(dis_sqt);
	for (min = mid_idx; min > start; min--)
	{
		if (arr[mid_idx].x - arr[min].x > dis)
			break;
	}
	for (max = mid_idx; max < end; max++)
    {
        if (arr[max].x - arr[mid_idx].x > dis)
            break;
    }
    min_sqt_value = ft_y_direction_min_sqt(arr, min, max, dis, dis_sqt);
    return (min_sqt_value);
}

int find_min_sqt(t_coor *arr, int min, int max)
{
    int i = max - min;
    int sqt1;
    int sqt2;
    int sqt3;
    int temp;
    int mid;
    
    if (i == 1) // 점이 2개
        return (ft_dis_sqt(arr[max], arr[min]));
    else if (i == 2) // 점이 3개
    {
        sqt1 = ft_dis_sqt(arr[min+1], arr[min]);
        sqt2 = ft_dis_sqt(arr[max], arr[max-1]);
        sqt3 = ft_dis_sqt(arr[max], arr[min]);
        temp = MIN(sqt1, sqt2);
        return (MIN(temp, sqt3));
    }
    else
    {
        mid = (max + min) / 2;
        sqt1 = find_min_sqt(arr, min, mid);
        sqt2 = find_min_sqt(arr, mid, max);
        temp = MIN(sqt1, sqt2);
        sqt3 = ft_min_dif(arr, min, max, mid, temp);
        return (MIN(temp, sqt3));
    }
}

int main()
{
    t_coor  *arr;
    int i;
    int j;
    int min_dis_sqt; // 최단거리

    scanf("%d", &i);
    arr = (t_coor *)malloc(sizeof(t_coor) * i);
    for (j=0; j<i; j++)
    {
        scanf("%d", &(arr[j].x));
        scanf("%d", &(arr[j].y));
    }
    qsort(arr, i, sizeof(t_coor), compare_x);
    min_dis_sqt = find_min_sqt(arr, 0, i-1);
    printf("%d", min_dis_sqt);
    free(arr);
    return 0;
}