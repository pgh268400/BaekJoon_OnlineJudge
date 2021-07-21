#include <stdio.h>
#include <stdlib.h>

int main(){
	int max, min = 0;
	int a,b,c;
	int tmp = 0;
	scanf("%d %d %d", &a, &b, &c);
	
	//1. 큰수를 먼저 맨오른쪽(c)으로 옮긴다.
	//2. a,b 두수를 정렬한다. 
	if(a > b){ //a가 b보다 클경우  
		tmp = a;
		a = b;
		b = tmp; //큰수를 b의 위치로 옮긴다. 
	}
	if(b > c){ //b가 c보다 클경우 
		tmp = b;
		b = c;
		c = tmp; //큰수를 c의 위치로 옮긴다. 
	}
	//여기까지 왔으면 큰수가 오른쪽으로 정렬되어 있다.
	if(a > b){ //a와 b의 정렬상태를 한번더 체크한다. 
		tmp = a;
		a = b;
		b = tmp; 
	} 

	
	
	printf("%d %d %d", a,b,c);
	
	return 0;
}