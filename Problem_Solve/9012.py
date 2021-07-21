repeat_time = int(input())

for i in range(repeat_time):
    strings = input()
    while True:
        if("()") in strings:
            strings = strings.replace("()", "")
        else:
            break
    if(strings != ""):
        print("NO")
    else:
        print("YES")