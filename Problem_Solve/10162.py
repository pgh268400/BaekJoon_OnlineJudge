#버튼은 각각 300초, 60초, 10초
A,B,C = 0,0,0
T = int(input())
backup_T = T
if(T >= 300):
    A = T // 300
    T = T % 300
    B = T // 60
    T = T % 60
    C = T // 10
elif(T >= 60):
    B = T // 60
    T = T % 60
    C = T // 10
elif(T >= 10):
    C = T // 10


if((A * 300 + B * 60 + C * 10) == backup_T):
    print(A,B,C)
else:
    print(-1)
    