lst = []
n = int(input())
for i in range(n):
    user = input().split()
    #참고 : i는 온 순서임
    lst.append((int(user[0]), i, user[1]))
lst.sort()
for age, index, name in lst:
    print(age, name)