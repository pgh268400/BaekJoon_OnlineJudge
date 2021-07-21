#include <stdio.h>
#include <string.h>

int main(void) {
    
    int input, score, sum;
    char strings[80];

    scanf("%d", &input);

    for(int i=0; i<input; i++) {
        sum = 0;
        score = 1;
        scanf("%s", strings);
        for(int j=0; j<strlen(strings); j++) {
            if(strings[j] == 'O') {
                sum += score;
                score++;
            }
            if(strings[j] == 'X') score = 1; //x를 만나면 누적을 1로 초기화 
        } 
        printf("%d\n", sum);
    }
}