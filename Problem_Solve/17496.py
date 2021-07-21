N,T,C,P = map(int , input().split())
ok_day = N // T
if(N % T == 0): #짝수로 나누어 떨어지면
    ok_day = ok_day - 1 #하나 차감해준다.
    result = ok_day * C * P
else:
    result = ok_day * C * P
print(result)