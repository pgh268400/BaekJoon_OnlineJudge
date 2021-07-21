#include <stdio.h>

int main(){
	int speed1, speed2;
	scanf("%d %d", &speed1, &speed2);
	int speed_gap = speed2 - speed1;
	if(speed_gap <= 0){
		printf("Congratulations, you are within the speed limit!");
	}else if(speed_gap >= 1 && speed_gap <= 20){
		printf("You are speeding and your fine is $100.");
	}else if(speed_gap >= 21 && speed_gap <= 30){
		printf("You are speeding and your fine is $270.");
	}else if(speed_gap >= 31){
		printf("You are speeding and your fine is $500.");
		
	}
	
	return 0;
}