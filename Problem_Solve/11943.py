A,B = map(int , input().split())
C,D = map(int , input().split())

print(min(A+D, B+C)) #대각선으로 swap 하는게 제일 효율적이다. 대각선 합이 적은쪽을 출력한다.