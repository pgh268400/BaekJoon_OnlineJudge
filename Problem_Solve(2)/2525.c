#include <stdio.h>
int main(){
	int hour, minute;
	int elapsed_time;
	scanf("%d %d", &hour, &minute);
	scanf("%d", &elapsed_time);
	
	//받은 분을 시와 분으로 변환한다. 
	int el_hour =  elapsed_time / 60;  
	int el_minute = elapsed_time % 60;
	
	//합에 반영한다. 
	hour += el_hour;
	minute += el_minute;
	
	//넘어간 분을 시에 반영한다
	hour += minute / 60;
	minute = minute % 60;

	//24:00을 넘어가버렸다면 
	if(hour >= 24 && minute >= 00){
		hour = hour - 24; //24를 빼줘서 0으로 clear 해준다. 
	}
	
	printf("%d %d", hour, minute);
	
	
	return 0;
}