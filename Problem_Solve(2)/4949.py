#4949번 - Stack을 이용한 풀이


while True:
    stack = []
    strings = input()
    
    if(strings == "."):
        break
    for s in strings:
        if(s == "("):
            stack.append("(")
        elif (s == "["):
            stack.append("[")
        elif (s == ")"):
            if(len(stack) == 0):
                stack.append(")")
            else:
                pop = stack.pop()
                if(pop == "("): #바로앞전에 쌓여있던것이 왼쪽 소괄호면
                    pass #없애고 넘어간다
                else:
                    stack.append(pop) #다시 추가해주고
                    stack.append(")") #방금 나온것도 추가해준다.
        elif (s == "]"):
            if(len(stack) == 0):
                stack.append("]")
            else:
                pop = stack.pop()
                if(pop == "["): 
                    pass 
                else:
                    stack.append(pop)
                    stack.append("]")
    #print(stack)
    if(len(stack) == 0):
        print("yes")
    else:
        print("no")