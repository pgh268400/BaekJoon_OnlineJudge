def dp(n):
    if(n == 0) : return 0
    elif(n == 1) : return 1
    elif(n == 2) : return 2
    elif(n == 3) : return 4
    else: return dp(n-3) + dp(n-2) + dp(n-1)
n = int(input())
for _ in range(n):
    num = int(input())
    print(dp(num))