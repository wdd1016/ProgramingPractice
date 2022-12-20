long long sum(int *a, int n) {
	long long ans = 0;
    while (n>0)
    {
        ans += *a;
        a++;
        n--;
    }
	return ans;
}
