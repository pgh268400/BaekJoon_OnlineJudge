#include <stdio.h>
#include <stdlib.h>

int main(){
	int a,b;
	scanf("%d %d", &a, &b);
	int result1 = (a + b) / 2;
	int result2 = (a - b) / 2;
	
	int chk1 = (a + b) % 2;
	int chk2 = (a - b) % 2;
	
	if(result1 < 0 || result2 < 0){
		printf("-1");
	}else if (chk1 != 0 || chk2!= 0){ //나누어떨어지지 않으면
		printf("-1");
	} else {
		if(result1 > result2){
			printf("%d %d", result1, result2);
		} else{
			printf("%d %d", result2, result1);
		}
	}
	
	
	return 0;
}