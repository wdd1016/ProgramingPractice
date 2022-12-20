#include <stdio.h>

int main()
{
	char score[3];
	scanf("%s", score);
	if (score[0] == 'F')
		printf("0.0");
	else
	{
		float f_score;
		f_score = 'E' - score[0];
		if (score[1] == '+')
			f_score += 0.3;
		else if (score[1] == '-')
			f_score -= 0.3;
		printf("%.1f", f_score);
	}
}