from sys import stdin
from collections import deque #deck 사용을 위해 import

#collections의 deque는 Cpython으로 구현되어있어서 그 속도가 훨씬 빠르다.

a = int(input())
queue = deque()

for i in range(1,a+1):
    queue.append(i)

while True:
    if(len(queue) == 1):
        break
    else:
        queue.popleft() #맨위에있는것을 버린다.
        queue.append(queue.popleft()) #뽑아서 제일 뒤로 옮긴다.
print(queue[0])