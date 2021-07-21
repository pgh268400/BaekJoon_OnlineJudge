#include <stdio.h>

int main(){
	int n, compare_n;
	scanf("%d %d", &n, &compare_n);
	int value;
	for (int i=1; i<=n; i++) 
	{
		scanf("%d", &value);
		if (value < compare_n) 
			printf("%d ", value);
	}
	
	return 0;
}