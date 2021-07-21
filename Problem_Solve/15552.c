#include <stdio.h>


int main(){
    int repeat_time, i = 1;
    scanf("%d", &repeat_time);
	for(; i<=repeat_time; i++) {
		int a,b;
		scanf("%d %d", &a, &b);
		printf("%d\n", a+b);
	}
	return 0;
}

