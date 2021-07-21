a = int(input())

minute = a // 5
minute2 = a % 5
if minute2 == 0:
    print(minute)
else:
    print(minute + 1)