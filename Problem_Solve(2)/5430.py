from collections import deque
from sys import stdin
input = stdin.readline

repeat = int(input().rstrip())
for i in range(repeat):
    reverse_flag = 1 #뒤집혀 있지 않음.
    command = input().rstrip()
    length = int(input().rstrip())
    deck = deque(input().rstrip().split(","))
    
    #양쪽 [, ] 뽑아서 제거해준다. -> deck은 양쪽 pop&append 의 시간복잡도가 O(1)
    
    if len(deck) == 1: #한개 들어온경우
        one = deck.pop()
        if one == "[]":
            pass
        else:
            deck.append(one.replace("[", "").replace("]", ""))
    else:
        left = deck.popleft()
        right = deck.pop()
        deck.appendleft(left.replace("[", ""))
        deck.append(right.replace("]", ""))
    
    error = False
    command = command.replace("RR", "") #연속뒤집기는 의미가 없으므로 제거함.
    for element in command:
        if element == "R":
            reverse_flag = reverse_flag * -1 #뒤집힘 상태에 -1을 곱해준다. 
        elif element == "D":
            if not deck: #비었으면
                error = True
                break
            else:
                if reverse_flag == -1: #뒤집혀 있으면
                    deck.pop() #맨 오른쪽걸 빼준다. (뒤집힌 상태서 빼는것 이므로.)
                else: #안뒤집혀 있으면
                    deck.popleft() #앞에걸 그냥 빼주면 된다.
    if(error == True):
        print("error")
    else:
        if reverse_flag == -1: #뒤집혀 있으면 거꾸로 출력해준다.
            deck.reverse() #뒤집는다.
            print(str(list(deck)).replace(" ", "").replace("'", ""))
        else:
            print(str(list(deck)).replace(" ", "").replace("'", ""))