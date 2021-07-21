#include <stdio.h>
int main(){
	int hour, minute;
	int sec;
	
	int elapsed_time;
	scanf("%d %d %d", &hour, &minute, &sec);
	scanf("%d", &elapsed_time);
	
	//받은 초를 분 / 초로 변환한다. 
	int el_minute =  elapsed_time / 60;  
	int el_sec = elapsed_time % 60;
	
	//합에 반영한다. 
	minute += el_minute;
	sec += el_sec;
	
	
	//넘어간 시간을 반영한다.
	
	minute += sec / 60;
	sec = sec % 60;
	 
	hour += minute / 60;
	minute = minute % 60;


	//24:00을 넘어가버렸다면 
	if(hour >= 24 && minute >= 00 && sec >= 00){
		hour = hour % 24; //24의 나머지로 clear해준다. 
	}
	
	printf("%d %d %d", hour, minute, sec);
	
	
	return 0;
}