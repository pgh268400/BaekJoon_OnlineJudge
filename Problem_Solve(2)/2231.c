#include <stdio.h>
int len_num(int n);

int main(){
	int check = 0;
	int save = 0;
	int n;
	int arr[7] = {0, };
	scanf("%d", &n);
	for(int i = 1; i <= n; i++){
		int a = i;
		
		int len = len_num(i);
		int sum_num = 0;
		sum_num += a % 10;
		for (int i = 0; i < len - 1; i++){
			a = a / 10;
			if(len_num(a) == 1){
				sum_num += a;
			} else {
				sum_num += a % 10;
			}
		}
		
		int creator = i + sum_num;
		
		if(n == creator){
			check = 1;
			save = i;
			break;
		}
	}

	if(check == 1){
		printf("%d", save);
	} else {
		printf("%d", 0);
	}
	return 0;
}

int len_num(int n){
	int idx = 0;
	int base = n;
	while(base != 0){
		base = base / 10;
		idx++;
	}
	return idx;
}