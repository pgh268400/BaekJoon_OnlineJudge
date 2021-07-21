#include <stdio.h>


int main(){
	int result1 = 0;
	int result2 = 0;
	
	int student1[4]; //민국 
	int student2[4]; //만세 
	
	for (int i = 0; i < 4; i++){
		//배열의 이름은 주소이나
		//각요소에 입력받을땐 & 기호를 붙여서 접근해야한다. 
		
		scanf("%d", &student1[i]);
		result1 += student1[i];
	}
	
	for (int i = 0; i < 4; i++){
		scanf("%d", &student2[i]);	
		result2 += student2[i];	
	}
	
	if(result1 > result2){
		printf("%d", result1);
	} else if(result1 < result2){
		printf("%d", result2);
	} else{ //동점일땐 민국이의 총점 출력 
		printf("%d", result1);
	}
	
	return 0;
}