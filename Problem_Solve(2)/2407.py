def factorial(n):
    if(n == 0):
        return 1
    elif(n < 3):
        return n
    return n * factorial(n - 1)
n, m = map(int, input().split())

m2 = min([n - m, m])

up = 1
for i in range(n, n - m2 , -1):
    up = up * i

down = factorial(m2)

print(up // down)