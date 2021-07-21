#include <stdio.h>


int main(){
	int a,b,c,d,p;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &d);
	scanf("%d", &p);
	
	int X_company = a * p; //X사 요금
	int Y_company = b; //기본요금이 b엔 
	
	if(p > c){ //사용량이 c리터가 넘었을 경우 
		Y_company += (p - c) * d; //C리터를 넘었을 경우 1리터를 넘었을때마다 D엔임. 
	}
	
	if(X_company > Y_company){
		printf("%d", Y_company);
	} else{
		printf("%d", X_company);
	}
	
	return 0;
}