from sys import stdin

lst = list(map(int, stdin.readline().rstrip().split()))

while True:
    c = max(lst)
    lst.remove(c)
    a = lst[0]
    b = lst[1]
    if (a == 0 and b == 0 and c == 0):
        break
    elif ((c ** 2) == ((a ** 2) + (b ** 2))):
        print("right")
    else:
        print("wrong")
    lst = list(map(int, stdin.readline().rstrip().split()))