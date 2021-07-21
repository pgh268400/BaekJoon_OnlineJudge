#include <stdio.h>

int main(){
	int c;
	scanf("%d", &c);
	for (int i=1; i<=c; i++) 
	{
		int a,b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d \n", i, a,b,a+b);
	}
	
	return 0;
}