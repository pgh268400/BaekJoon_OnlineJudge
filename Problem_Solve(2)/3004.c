#include <stdio.h>
#include <stdlib.h>

int main(){
	int n;
	scanf("%d", &n);
	int t = (n / 2) + 1;

	if (n % 2 == 0){
		printf("%d", t * t);
	} else {
		printf("%d", t * (t + 1));
	}
	
	return 0;
}