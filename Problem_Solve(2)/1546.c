#include <stdio.h>
int get_max(int score_array[]);
double change_score_avg(int score_array[]);

int length;
int main(){
	int score[1000];
	scanf("%d", &length);
	for (int i = 0; i < length; i++)
		scanf("%d", &score[i]);
	printf("%f", change_score_avg(score));
	return 0;
}


int get_max(int score_array[]){
	if(length == 0)
		return score_array[0]; //한개밖에없으면 첫번째 것이 최대값. 
	int result = score_array[0];

	for (int i = 1; i < length; i++){
		if (result < score_array[i]) result = score_array[i];
	}
	return result;
}

double change_score_avg(int score_array[]){

	int array_max = get_max(score_array);
	double new_score_array[1000];
	double avg = 0;

	for (int i = 0; i < length; i++){
		//점수 고치기 Logic 
		new_score_array[i] = (double)score_array[i] / array_max * 100; 
		
	}
	
	for (int i = 0; i < length; i++){
		avg += new_score_array[i];
	}
	avg = avg / length;
	return avg;
}