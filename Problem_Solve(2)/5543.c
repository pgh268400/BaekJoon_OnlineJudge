#include <stdio.h>


int main(){
	int min_burger, min_soda;
	int burger1, burger2, burger3, soda1, soda2;
	scanf("%d", &burger1);
	scanf("%d", &burger2);
 	scanf("%d", &burger3);
 	scanf("%d", &soda1);
 	scanf("%d", &soda2);
 	
 	min_burger = burger1;
 	min_soda = soda1;
	
	if(min_burger > burger2){
		min_burger = burger2;
	}
	if(min_burger > burger3){
		min_burger = burger3;
	}
	
	if(min_soda > soda2){
		min_soda = soda2;
	}
	
	printf("%d", min_burger + min_soda - 50);

	 
	return 0;
}