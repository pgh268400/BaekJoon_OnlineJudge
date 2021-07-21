#include <stdio.h>
int cycle(int n);

int main(){
	int n, m, count = 0;
	scanf("%d", &n);
	
	m = n; 
	while(cycle(n) != m){
		count += 1;
		//printf("%d \n", cycle(n));
		n = cycle(n);
		}
	printf("%d", count+1);
	return 0;
}

int cycle(int n){
	int n10 = n/10; //10의자리 
	int n1 = n%10; //1의자리 
		
	int sum = n10 + n1;
	sum = sum % 10; //합에서 오른쪽숫자 (1의 자리만 가져온다) 	
	int result = n1 * 10 + sum; //새로운 수 제작 
	return result;
}