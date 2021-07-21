#include <stdio.h>

long long factorial(long long n){
	if(n == 0) return 1;
	else if(n < 3) return n;
	return n * factorial(n-1);
}

int main(){
	long long result = 0;
	long long n=0, k=0;
	scanf("%d %d", &n, &k);
	
	result = factorial(n) / (factorial(k) * factorial(n - k));
	printf("%lld", result);
	return 0;
}