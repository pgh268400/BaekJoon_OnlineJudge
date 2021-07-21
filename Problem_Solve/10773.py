from sys import stdin
lst = []
repeat_time = int(stdin.readline().rstrip())

for i in range(repeat_time):
    num = int(stdin.readline().rstrip())
    if(num == 0):
        del lst[-1]
    else:
        lst.append(num)
print(sum(lst))