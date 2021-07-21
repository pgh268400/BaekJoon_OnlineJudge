#include <stdio.h>

int main(){
	int D,H,M;
	scanf("%d %d %d", &D, &H, &M);
	int t1 = D * 24 * 60 + H * 60 + M;
	int t2 = 11 * 24 * 60 + 11 * 60 + 11;
	int elasped_time = t1 - t2;
	if(t2 > t1){
		printf("-1");
	} else {
		printf("%d", elasped_time);
	}

	return 0;
}