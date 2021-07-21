#include <stdio.h>

int main(){
	int a,b,c,d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	//차이를 최대한 줄이려면 제일 큰것 + 제일 작은것
	//중간크기 2개로 해야 차이가 제일 적어짐.
	//a,b,c,d는 자동 정렬해서 데이터를 주기땜에 정렬 구현 필요없음.
	
	int distance = (d+a) - (b+c);
	distance = distance < 0 ? distance * (-1) : distance;
	printf("%d", distance);
	return 0;
}