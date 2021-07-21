#include <stdio.h>

int main(){
	int c;
	scanf("%d", &c);
	for (int i=1; i<=c; i++) {
		for(int j=1; j<=(c-i); j++) printf(" ");
		for(int k=1; k<=i; k++) printf("*");
		printf("\n");
	}
	return 0;
}