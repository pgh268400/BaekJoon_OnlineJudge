#include <stdio.h>

void get_work_time(){
	int start_hour, start_minute, start_sec;
	int end_hour, end_minute, end_sec;
	scanf("%d %d %d %d %d %d", &start_hour, &start_minute, &start_sec , &end_hour , &end_minute, &end_sec);
	
	int work_hour = end_hour - start_hour;
	int work_minute = end_minute - start_minute;
	int work_sec = end_sec - start_sec;
	
	if(work_sec < 0){ //일한 초가 음수면 
		work_sec = 60 + work_sec; //60으로 우선 반전시킨다. 
		work_minute--; //분에서 차감시킨다. 
	}
	
	if(work_minute < 0){ //처리후 일한 분이 음수면 
		work_minute = 60 + work_minute; //60으로 우선 반전시킨다. 
		work_hour--; //시에서 차감시킨다. 
	}
	printf("%d %d %d\n", work_hour, work_minute, work_sec);
}

int main(){
	get_work_time();
	get_work_time();
	get_work_time();
	
	return 0;
}