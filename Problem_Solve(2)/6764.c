#include <stdio.h>

void BubbleSort(int arr[], int n)
{
	int i, j;
	int temp; //데이터 교환을 위한 변수

	for (i = 0; i < n - 1; i++)
	{
		for (j = 0; j < (n - i) - 1; j++)
		{
			if (arr[j] > arr[j + 1])	// 오름차순
			{
				//swap
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

int check_fish(int depth[]){

	//0 == rising, 1 == diving, 2 == no fish
		int count = 0;
		for(int i = 0; i < 3; i++){
		if(depth[i] < depth[i+1]){
			count++;
		}
	}
		
		if (count == 3){
			return 0;
		} else {
			count = 0;
			for(int i = 0; i < 3; i++){
		if(depth[i] > depth[i+1]){
			count++;
		}
		}
		
			if (count == 3){
			return 1;
		} else {
			return 2;
		}
		
	}
		
}


int main(){
	int status = 0;
	int depth[4] = {0, };
	scanf("%d", &depth[0]);
	scanf("%d", &depth[1]);
	scanf("%d", &depth[2]);
	scanf("%d", &depth[3]);

	if(depth[0] == depth[1] && depth[1] == depth[2] && depth[2] == depth[3]){
		printf("Fish At Constant Depth");
	} else {
		int check = check_fish(depth);
		if(check == 0){
			printf("Fish Rising");
		}else if (check == 1){
			printf("Fish Diving");
		}else{
			printf("No Fish");
		}
	}

		
	
	return 0;
}