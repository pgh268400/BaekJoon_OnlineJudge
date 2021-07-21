#include <stdio.h>


int main(){
	
	int repeat_count;
	scanf("%d", &repeat_count);
	
	for (int i = 0; i < repeat_count; i++){
			int h,w,n;
			scanf("%d %d %d", &h, &w, &n);
			int start = n % h;
			int end = n / h + 1;
			
			if (start == 0){ //나머지가 0인경우 (맨위층으로 생각한다.) 
				start = h;  
				end = end - 1; //끝 번호도 1빼줘야 한다. (몫이 잘 떨어진다.) 
				
			}
			
			//방번호는 YXX나 YYXX 형태임.
			if(end / 10 == 0){ //한자리수면  
				printf("%d0%d\n", start, end); //중간에 0껴서 출력해준다. 
			} else { //그게 아니면 그냥 출력한다. 
				printf("%d%d\n",start,end);
			}
	}
	

	 
	
	
	return 0;
}