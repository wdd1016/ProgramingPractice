#include <stdio.h>

int ft_bad(int i, int *cnt)
{
    if (i <= 2)
    {
        (*cnt)++;
        return 1;
    }
    else
       return (ft_bad(i-1, cnt) + ft_bad(i-2, cnt));
}

int ft_good(int i, int *cnt, int *fd)
{
    if (i <= 2)
    {
        return 1;
    }
    else if (fd[i] == 0)
    {
        fd[i] = ft_good(i-1, cnt, fd) + ft_good(i-2, cnt, fd);
        (*cnt)++;
    }
    return fd[i];
}

int main()
{
    int i;
    int cnt;
    int cnt2;
    int fd[50] = {0, };
    
    cnt = 0;
    cnt2 = 0;
    scanf("%d", &i);
    fd[1] = 1;
    fd[2] = 1;
    ft_bad(i, &cnt);
    ft_good(i, &cnt2, fd);
    printf("%d %d", cnt, cnt2);
}