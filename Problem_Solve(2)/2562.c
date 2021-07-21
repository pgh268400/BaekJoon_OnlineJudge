#include <stdio.h>

int cycle(int n);

int main(){
	int n[9];
	int max, a, idx=1;
	
	for(int i = 0; i < 9; i++)
	{
		scanf("%d", &a);
		n[i] = a;
		if (i == 0) max = a; //첫번째 넣은수를 최대로 
		if (max < a)
		{
			max = a;
		} 
	}
	
		for(int i = 0; i < 9; i++)
	{
		if(n[i] == max) break;
		idx += 1;
	}
	printf("%d\n", max);
	printf("%d", idx);
	return 0;
}
