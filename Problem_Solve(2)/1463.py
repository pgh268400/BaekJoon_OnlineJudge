n = int(input())
lst = [-1,0,1,1]
def dp(n):
    if(n == 1) : return 0
    elif(n == 2) : return 1
    elif(n == 3) : return 1
    else:
        for i in range(4, n+1):
            a,b,c = 9999999,9999999,9999999
            if(i % 3 == 0): a = lst[i//3] + 1
            if(i % 2 == 0): b = lst[i//2] + 1
            c = lst[i-1] + 1
            lst.append(min([a,b,c]))
        return lst[-1]
print(dp(n)) 