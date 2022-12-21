#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	struct tm *date;
	const time_t now_time = time(NULL) + (3600 * 9);

	date = localtime(&now_time);
	printf("%d-%d-%d", date->tm_year + 1900, date->tm_mon + 1, \
	date->tm_mday);

	return 0;
}