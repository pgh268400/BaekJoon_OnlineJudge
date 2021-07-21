from sys import stdin

repeat_time = int(stdin.readline().rstrip())
deck = []
for i in range(repeat_time):
    command = stdin.readline().rstrip()
    if 'push_front' in command:
        command = command.split()
        deck.insert(0, int(command[1]))
    elif 'push_back' in command:
        command = command.split()
        deck.append(int(command[1])) #append는 맨뒤에 요소를 추가함
    elif command == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            element = deck[0]
            del deck[0]
            print(element)
    elif command == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            element = deck[-1]
            del deck[-1]
            print(element)
    elif command == 'size':
        print(len(deck))
    elif command == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif command == 'back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])