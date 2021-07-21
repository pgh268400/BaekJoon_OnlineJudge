from sys import stdin
input = stdin.readline

dic = {}
N,M = map(int, input().rstrip().split())
for i in range(1, N+1):
    txt = input().rstrip()
    #문자가 와도 찾을 수 있게 번호도 미리 추가해둠.
    dic[i] = txt
    dic[txt] = i

for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdigit(): #숫자라면
        print(dic[int(quiz)]) #딕셔너리에서 꺼내옴
    else:
        print(dic[quiz])