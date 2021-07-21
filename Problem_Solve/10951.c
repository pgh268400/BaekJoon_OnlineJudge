#include <stdio.h>

int main(){
	int a,b;
	
	while(scanf("%d %d", &a, &b) != EOF){ //조건문이 참 거짓인지를 판별하기위해 실행 
		printf("%d\n", a+b);
	}
	return 0;
}