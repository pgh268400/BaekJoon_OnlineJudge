a = int(input())
for i in range(a):
    lst = input().split()
    repeat_count = int(lst[0])
    for char in lst[1]:
        print(char * repeat_count, end="")
    print()