from sys import stdin
repeat_time = int(stdin.readline().rstrip())
stack = []
for i in range(repeat_time):
    command = stdin.readline().rstrip()
    if 'push' in command:
        command = command.split()
        stack.append(int(command[1]))
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            element = stack[-1]
            del stack[-1]
            print(element)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])