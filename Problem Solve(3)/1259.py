a = input()
while (a != "0"):
    if(a == a[::-1]):
        print("yes")
    else:
        print("no")
    a = input()