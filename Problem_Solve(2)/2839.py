sugar = int(input())

lst = []
case1 = sugar % 5
case2 = sugar % 3

if(case1 == 0): #5의 배수면
    lst.append(sugar // 5)
if(case2 == 0): #3의 배수면
    lst.append(sugar // 3)

tmp = sugar 
for i in range(sugar // 5 + 1):
    tmp -= 5 #5씩 차감해간다
    if(tmp < 0):
        break
    if(tmp % 3 == 0): #3의 배수가 잡힐때마다 추가한다.
        lst.append(i + 1 + tmp // 3)

if(len(lst) == 0):
    print(-1)
else:
    print(min(lst))