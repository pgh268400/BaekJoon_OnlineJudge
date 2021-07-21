#include <stdio.h>
#include <limits.h>

int cycle(int n);

int main(){
	int a, n, max, min = INT_MAX;
	scanf("%d", &n);
	
	for(int i = 1; i <= n; i++)
	{
		scanf("%d", &a);
		if (i == 1) max = a; //첫번째 넣은수를 최대로 
		if (max < a) max = a;
		if (min > a) min = a;
	}
	printf("%d %d", min, max);
	return 0;
}

