#include <stdio.h>
#include <stdlib.h>

int main(){
	int elapse_time1 = 0;
	int elapse_time2 = 0;
	int cant_play_time = 0;
	int L,A,B,C,D;
	scanf("%d", &L);
	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);
	scanf("%d", &D);
	
	elapse_time1 = A / C;
	elapse_time2 = B / D;
	
	//나누어 떨어지지 않으면 1일 더걸린다. 
	if(A % C != 0) elapse_time1++;
	if(B % D != 0) elapse_time2++;
	
	//두 과제가 몇일이 걸리던 더 오래걸리는쪽만큼 못논다
	//ex) 각각 6일 / 10일안에 끝내도 10일간은 못놈. 
	if(elapse_time1 > elapse_time2){
		cant_play_time = elapse_time1;
	} else {
		cant_play_time = elapse_time2;
	}
	
	printf("%d", L - cant_play_time);
	
	
	return 0;
}