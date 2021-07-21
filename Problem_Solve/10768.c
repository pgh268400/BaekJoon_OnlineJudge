#include <stdio.h>


int main(){
	int month, day;
	scanf("%d", &month);
	scanf("%d", &day);
	
	if(month == 1 && day <= 31){
		printf("Before");
	} else if(month == 2 && day < 18) {
		printf("Before");
	} else if(month == 2 && day == 18){
		printf("Special");
	} else {
		printf("After");
	}

	return 0;
}