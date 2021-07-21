from sys import stdin
#stdin.readline().rstrip()
repeat_time = int(stdin.readline().rstrip())
que = []
for i in range(repeat_time):
    command = stdin.readline().rstrip()
    if 'push' in command:
        command = command.split()
        que.append(int(command[1]))
    elif command == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            element = que[0]
            del que[0]
            print(element)
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif command == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])