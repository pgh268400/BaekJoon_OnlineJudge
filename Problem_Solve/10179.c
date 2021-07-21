#include <stdio.h>


int main(){
	int test_case = 0;
	scanf("%d", &test_case);
	
	for(int i = 0; i < test_case; i++){
		double price;
		scanf("%lf", &price);
		printf("$%.2f\n", price * 0.80);
	}
	return 0;
}