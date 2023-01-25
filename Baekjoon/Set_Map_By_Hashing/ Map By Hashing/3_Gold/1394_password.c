#include <stdio.h>
#include <string.h>

int main()
{
	char str[101];
	char solution[1000001];
	int len_str, len_sol;
	int map[256] = {0, };

	scanf("%s", str);
	scanf("%s", solution);
	len_str = strlen(str);
	len_sol = strlen(solution);
	for (int i = 0; i < len_str; i++)
	{
		map[str[i]] = i; // str[i]의 문자의 아스키코드값을 index로 갖는 해쉬배열
	}
	int answer1 = 0; // 대입할때의 글자개수가 len_sol 보다 작을때의 시도횟수
	int answer2 = 0; // answer2는 대입할때의 글자개수가 len_sol일때의 시도횟수
	for (int j = 0; j < len_sol; j++)
	{
		if (j < len_sol - 1)
			answer1 = (answer1 * len_str) + len_str;
		if (answer1 >= 900528)
			answer1 %= 900528;
		answer2 = (answer2 * len_str) + map[solution[j]];
		if (answer2 >= 900528)
			answer2 %= 900528;
	}
	printf("%d\n", (answer1 + answer2 + 1) % 900528);
}