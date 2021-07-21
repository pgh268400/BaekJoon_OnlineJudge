doit = True
stack = []
history = []

tmp = 1
n = int(input())

for i in range(n):
    num = int(input())
    while tmp <= num: #입력한 수에 도달할때까지 반복함
        stack.append(tmp)
        history.append("+")
        tmp += 1
        
    if (stack[-1] == num):
        stack.pop()
        history.append("-")
    else: #맨위에서 뽑을 수 없다면 이것은 만들 수 없는 수열이다.
        doit = False
        break
if(doit):
    for element in history:
        print(element)
else:
    print("NO")