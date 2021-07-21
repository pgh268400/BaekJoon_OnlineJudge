#에라토스테네스의 체
import math

m,n = map(int , input().split())
lst = [i for i in range(m,n+1)]
lst = set(lst) #집합 자료형으로 변환
if 1 in lst:
    lst.remove(1) #1을 제거한다

for i in range(2, int(math.sqrt(n) + 1)):
        #배수를 반복문 돌려서 전부 지워준다.
        j = 2
        while (i * j <= n):
            if i * j in lst:
                lst.remove(i * j)
            j += 1 
lst = list(lst)
lst.sort()
for item in lst:
    print(item)